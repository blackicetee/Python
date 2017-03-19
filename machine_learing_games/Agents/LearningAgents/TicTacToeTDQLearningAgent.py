import sqlite3
from operator import itemgetter

import logging
from random import randint

from machine_learing_games.tictactoe.TicTacToe import TicTacToe
from machine_learing_games.tictactoe.TicTacToeZobrist import TicTacToeZobrist

TICTACTOE_3x3_TDQ_AGENT_100_NAME = '3x3_ttt_tdq_agent_100_.db'
TICTACTOE_3x3_TDQ_AGENT_1000_NAME = '3x3_ttt_tdq_agent_1000_.db'
TICTACTOE_3x3_TDQ_AGENT_10000_NAME = '3x3_ttt_tdq_agent_10000_.db'

TICTACTOE_4x4_TDQ_AGENT_100_NAME = '4x4_ttt_tdq_agent_100_.db'
TICTACTOE_4x4_TDQ_AGENT_1000_NAME = '4x4_ttt_tdq_agent_1000_.db'
TICTACTOE_4x4_TDQ_AGENT_10000_NAME = '4x4_ttt_tdq_agent_10000_.db'

class TicTacToeTDQLearningAgent:
    def __init__(self, TicTacToeDBName, ticTacToeDimension):
        logging.basicConfig(filename=str(TicTacToeDBName).replace(".db", "Log"),
                            filemode='a',
                            format='%(asctime)s,%(msecs)d %(name)s %(levelname)s %(message)s',
                            datefmt='%H:%M:%S',
                            level=logging.DEBUG)
        self.__DBCursor = None
        self.__DBConnection = None
        self.createDB(TicTacToeDBName)
        self.__s = None
        self.__a = None
        self.__r = None
        self.__dimension = ticTacToeDimension
        self.__random_factor = 0
        self.__zobristHash = TicTacToeZobrist()
        if self.__dimension == 3:
            self.__zobristHash.set_zobrist_board_positoin_array(
                TicTacToeZobrist().getFixed9FieldTicTacToeZobristBoardPositionArray())
        elif self.__dimension == 4:
            self.__zobristHash.set_zobrist_board_positoin_array(
                TicTacToeZobrist().getFixed16FieldTicTacToeZobristBoardPositionArray())

    def explorationStrategy(self, ticTacToeState):
        if not ticTacToeState.is_terminal():
            depth = ticTacToeState.count_of_game_tokens_in_game()
            if randint(0, self.__random_factor * depth) == randint(0, self.__random_factor * depth) and depth < (2 * self.__dimension):
                moves = ticTacToeState.get_possible_moves()
                return moves[randint(0, (len(moves) - 1))]
            else:
                return self.suggestAction(ticTacToeState)
        else:
            return None

    def learnTictactoe(self, gamesToPlay):
        for gameCount in range(gamesToPlay):
            ttt = TicTacToe(self.__dimension)
            logging.info('Learning against itself game: ' + str(gameCount))
            while not ttt.is_terminal():
                suggestedAction = self.qLearnIteration(ttt, ttt.getReward(), 0.4, 1)
                ttt.make_move(suggestedAction)
            if ttt.is_terminal():
                self.qLearnIteration(ttt, ttt.getReward(), 0.4, 1)
            self.__s = None
            self.__a = None
            self.__r = None
            if gameCount % 100 == 0:
                self.__random_factor += 1

    def suggestAction(self, state):
        ticTacToeStateHash = self.__zobristHash.get_hash(state.game_matrix)
        self.__DBCursor.execute("SELECT * FROM Q WHERE ticTacToeStateHash = ?", [ticTacToeStateHash])
        listOfQEntries = self.__DBCursor.fetchall()
        if not len(listOfQEntries) > 0:
            return state.get_possible_moves()[0]
        if state.get_player_to_move() == 'X':
            maxQEntry = max(listOfQEntries, key=itemgetter(2))
        else:
            maxQEntry = min(listOfQEntries, key=itemgetter(2))
        return self.translateActionTupleString2IntTuple(str(maxQEntry[1]))

    def qLearnIteration(self, sPrime, rPrime, alpha, gamma):
        if sPrime.is_terminal():
            self.insertActionValueInQ(sPrime, None, rPrime)
        if self.__s is not None:
            qActionValue = self.getActionValueFromQ(self.__s, self.__a)
            maxActionValue = self.maxActionValueForAllActionsInSPrime(sPrime)
            qValueUpdate = qActionValue + alpha * (self.__r + gamma * maxActionValue - qActionValue)
            self.insertActionValueInQ(self.__s, self.__a, qValueUpdate)
            logging.info('\nUpdate Q-Value:')
            logging.info(
                'Q(' + str(self.__zobristHash.get_hash(self.__s.game_matrix)) + ', ' + str(self.__a) + ') <-- ' + str(
                    qActionValue) + ' + ' + str(alpha) + '(' + str(self.__r) + ' + ' + str(gamma) + ' * ' + str(
                    maxActionValue) + ' - ' + str(qActionValue) + ') = ' + str(qValueUpdate))
            logging.info('\n' + sPrime.printable_game_matrix())
            logging.info(self.__zobristHash.get_hash(sPrime.game_matrix))

        else:
            self.__s = TicTacToe(self.__dimension)
        self.__s.initialize_game_with_another_game(sPrime)
        self.__a = self.explorationStrategy(sPrime)
        self.__r = rPrime
        return self.__a

        ###########################################################################
        ###                     AGENT EXPERIENCE FUNCTIONS                      ###
        ###########################################################################

    def createDB(self, TicTacToeDBName):
        self.__DBConnection = sqlite3.connect(TicTacToeDBName)
        self.__DBCursor = self.__DBConnection.cursor()
        self.__DBCursor.execute(
            'CREATE TABLE IF NOT EXISTS Q(tictacToeStateHash INTEGER, actionInState TEXT, actionValue REAL)')

    def insertActionValueInQ(self, sPrime, actionInState, actionValue):
        ticTacToeStateHash = self.__zobristHash.get_hash(sPrime.game_matrix)
        actionInState = str(actionInState)
        if self.isStateActionPairInQ(ticTacToeStateHash, actionInState):
            self.__DBCursor.execute("UPDATE Q Set actionValue = ? WHERE ticTacToeStateHash = ? AND actionInState = ?",
                                    [actionValue, ticTacToeStateHash, actionInState])
        else:
            self.__DBCursor.execute("INSERT INTO Q(ticTacToeStateHash, actionInState, actionValue) VALUES (?, ?, ?)",
                                    (ticTacToeStateHash, actionInState, actionValue))
        self.__DBConnection.commit()

    def getActionValueFromQ(self, sPrime, actionInState):
        ticTacToeStateHash = self.__zobristHash.get_hash(sPrime.game_matrix)
        actionInState = str(actionInState)
        self.__DBCursor.execute(
            "SELECT actionValue FROM Q WHERE ticTacToeStateHash = ? AND actionInState = ?",
            [ticTacToeStateHash, actionInState])
        results = self.__DBCursor.fetchall()
        if len(results) > 0:
            return results[0][0]
        else:
            self.insertActionValueInQ(sPrime, actionInState, 0)
            return 0

    def maxActionValueForAllActionsInSPrime(self, sPrime):
        if not sPrime.is_terminal():
            allActionsInSPrime = sPrime.get_possible_moves()
            maxActionValue = self.getActionValueFromQ(sPrime, allActionsInSPrime[0])
            for action in allActionsInSPrime:
                maxActionValue = max(maxActionValue, self.getActionValueFromQ(sPrime, action))
            return maxActionValue
        else:
            return sPrime.getReward()

    def getMaxActionInStateFromQ(self, sPrime):
        ticTacToeStateHash = self.__zobristHash.get_hash(sPrime.game_matrix)
        self.__DBCursor.execute("SELECT * FROM Q WHERE ticTacToeStateHash = ?", [ticTacToeStateHash])
        listOfQEntries = self.__DBCursor.fetchall()
        if not len(listOfQEntries) > 0:
            self.maxActionValueForAllActionsInSPrime(sPrime)
            self.__DBCursor.execute("SELECT * FROM Q WHERE ticTacToeStateHash = ?", [ticTacToeStateHash])
            listOfQEntries = self.__DBCursor.fetchall()
        maxQEntry = max(listOfQEntries, key=itemgetter(2))
        return self.translateActionTupleString2IntTuple(str(maxQEntry[1]))

    def minActionValueForAllActionsInSPrime(self, sPrime):
        if not sPrime.is_terminal():
            allActionsInSPrime = sPrime.get_possible_moves()
            minActionValue = self.getActionValueFromQ(sPrime, allActionsInSPrime[0])
            for action in allActionsInSPrime:
                minActionValue = min(minActionValue, self.getActionValueFromQ(sPrime, action))
            return minActionValue
        else:
            return sPrime.getReward()

    def getMinActionInStateFromQ(self, sPrime):
        ticTacToeStateHash = self.__zobristHash.get_hash(sPrime.game_matrix)
        self.__DBCursor.execute("SELECT * FROM Q WHERE ticTacToeStateHash = ?", [ticTacToeStateHash])
        listOfQEntries = self.__DBCursor.fetchall()
        if not len(listOfQEntries) > 0:
            self.minActionValueForAllActionsInSPrime(sPrime)
            self.__DBCursor.execute("SELECT * FROM Q WHERE ticTacToeStateHash = ?", [ticTacToeStateHash])
            listOfQEntries = self.__DBCursor.fetchall()
        maxQEntry = min(listOfQEntries, key=itemgetter(2))
        return self.translateActionTupleString2IntTuple(str(maxQEntry[1]))

    def isStateActionPairInQ(self, ticTacToeStateHash, actionInState):
        self.__DBCursor.execute("SELECT * FROM Q WHERE ticTacToeStateHash = ? AND actionInState = ?",
                                [ticTacToeStateHash, actionInState])
        if len(self.__DBCursor.fetchall()) == 0:
            return False
        else:
            return True

    def translateActionTupleString2IntTuple(self, stringActionTuple):
        tupleStringValues = stringActionTuple.translate(None, '( )').split(',')
        return (int(tupleStringValues[0]), int(tupleStringValues[1]))

    def incrementStateActionPairFrequenceInN(self, sPrime, actionInState):
        actionInState = str(actionInState)
        ticTacToeStateHash = self.__zobristHash.get_hash(sPrime.game_matrix)
        stateActionPairFrequence = self.getStateActionPairFrequenceFromN(sPrime, actionInState)
        if stateActionPairFrequence is not None:
            stateActionPairFrequence += 1
            self.__DBCursor.execute(
                "UPDATE N Set stateActionPairFrequence = ? WHERE ticTacToeStateHash = ? AND actionInState = ?",
                [stateActionPairFrequence, ticTacToeStateHash, actionInState])
        else:
            self.__DBCursor.execute(
                "INSERT INTO N(ticTacToeStateHash, actionInState, stateActionPairFrequence) VALUES (?, ?, ?)",
                (ticTacToeStateHash, actionInState, 1))
        self.__DBConnection.commit()

    def getStateActionPairFrequenceFromN(self, sPrime, actionInState):
        ticTacToeStateHash = self.__zobristHash.get_hash(sPrime.game_matrix)
        actionInState = str(actionInState)
        self.__DBCursor.execute(
            "SELECT stateActionPairFrequence FROM N WHERE ticTacToeStateHash = ? AND actionInState = ?",
            [ticTacToeStateHash, actionInState])
        results = self.__DBCursor.fetchall()
        if len(results) > 0:
            return results[0][0]
        else:
            return None

    def getLeastVisitedActionInStateFromN(self, ticTacToeState):
        leastVisitedActionState = None
        minVisits = 1000
        possible_actions = ticTacToeState.get_possible_moves()
        for action in possible_actions:
            frequence = self.getStateActionPairFrequenceFromN(ticTacToeState, action)
            if frequence is None:
                frequence = 0
            if frequence < minVisits:
                minVisits = frequence
                leastVisitedActionState = action
        return leastVisitedActionState

    def isStateActionPairInN(self, ticTacToeStateHash, actionInState):
        self.__DBCursor.execute("SELECT * FROM N WHERE ticTacToeStateHash = ? AND actionInState = ?",
                                [ticTacToeStateHash, actionInState])
        if len(self.__DBCursor.fetchall()) == 0:
            return False
        else:
            return True

    def closeDB(self):
        self.__DBCursor.close()
        self.__DBConnection.close()

        ###########################################################################
        ###                     FIXED LEARNING FUNCTIONS                        ###
        ###########################################################################

    def train3x3TicTacToeAgentIn100Games(self):
        agent = TicTacToeTDQLearningAgent(TICTACTOE_3x3_TDQ_AGENT_100_NAME, 3)
        agent.learnTictactoe(100)
        agent.closeDB()

    def train3x3TicTacToeAgentIn1000Games(self):
        agent = TicTacToeTDQLearningAgent(TICTACTOE_3x3_TDQ_AGENT_1000_NAME, 3)
        agent.learnTictactoe(1000)
        agent.closeDB()

    def train3x3TicTacToeAgentIn10000Games(self):
        agent = TicTacToeTDQLearningAgent(TICTACTOE_3x3_TDQ_AGENT_10000_NAME, 3)
        agent.learnTictactoe(10000)
        agent.closeDB()

    def train4x4TicTacToeAgentIn100Games(self):
        agent = TicTacToeTDQLearningAgent(TICTACTOE_4x4_TDQ_AGENT_100_NAME, 4)
        agent.learnTictactoe(100)
        agent.closeDB()

    def train4x4TicTacToeAgentIn1000Games(self):
        agent = TicTacToeTDQLearningAgent(TICTACTOE_4x4_TDQ_AGENT_1000_NAME, 4)
        agent.learnTictactoe(1000)
        agent.closeDB()

    def train4x4TicTacToeAgentIn10000Games(self):
        agent = TicTacToeTDQLearningAgent(TICTACTOE_4x4_TDQ_AGENT_10000_NAME, 4)
        agent.learnTictactoe(10000)
        agent.closeDB()