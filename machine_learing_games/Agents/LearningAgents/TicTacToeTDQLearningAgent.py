import sqlite3
from operator import itemgetter

import logging
from random import randint

from machine_learing_games.tictactoe.TicTacToe import TicTacToe
from machine_learing_games.tictactoe.TicTacToeZobrist import TicTacToeZobrist



class TDQLearningAgentTicTacToe:
    def __init__(self, TicTacToeDBName):
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
        self.__random_factor = 0
        self.__count_random_actions = 0
        self.__count_not_random_actions = 0
        self.__zobristHash = TicTacToeZobrist()
        self.__zobristHash.set_zobrist_board_positoin_array(TicTacToeZobrist().getFixed9FieldTicTacToeZobristBoardPositionArray())

    def explorationStrategy(self, ticTacToeState):
        actionWithMaxQValue = self.getMaxActionInStateFromQ(ticTacToeState)
        depth = ticTacToeState.count_of_game_tokens_in_game()
        if randint(0, self.__random_factor * depth) == randint(0, self.__random_factor * depth):
            moves = ticTacToeState.get_possible_moves()
            self.__count_random_actions += 1
            return moves[randint(0, (len(moves) - 1))]
        else:
            self.__count_not_random_actions += 1
            return actionWithMaxQValue

    def learn3x3Tictactoe(self, gamesToPlay):
        for gameCount in range(gamesToPlay):
            ttt = TicTacToe(3)
            logging.info('Learning against itself game: ' + str(gameCount))
            while not ttt.is_terminal():
                suggestedAction = self.qLearnIteration(ttt, ttt.getReward(), 0.1, 1)
                logging.info('\n' + ttt.printable_game_matrix())
                logging.info(self.__zobristHash.get_hash(ttt.game_matrix))
                logging.info(suggestedAction)
                ttt.make_move(suggestedAction)
                print 'Count random actions: ' + str(self.__count_random_actions)
                print 'Count not random actions: ' + str(self.__count_not_random_actions)
            if ttt.is_terminal():
                self.qLearnIteration(ttt, ttt.getReward(), 0.1, 1)
                print 'Game Count: ' + str(gameCount)
                print ttt.printable_game_matrix()
            self.__s = None
            self.__a = None
            self.__r = None
            if gameCount % 50 == 0:
                self.__random_factor += 1

    def suggestAction(self, state):
        return self.getMaxActionInStateFromQ(state)

    #https://www.youtube.com/watch?v=1XRahNzA5bE
    # with N Table
    def qLearnIteration(self, sPrime, rPrime, alpha, gamma):
        if sPrime.is_terminal():
            self.insertActionValueInQ(sPrime, None, rPrime)
            if self.__s is not None:
                self.incrementStateActionPairFrequenceInN(self.__s, self.__a)
                self.insertActionValueInQ(self.__s, self.__a,
                                          self.getActionValueFromQ(self.__s, self.__a)
                                          + alpha * self.getStateActionPairFrequenceFromN(self.__s, self.__a)
                                          * (self.__r + gamma * rPrime - self.getActionValueFromQ(self.__s, self.__a)))
        else:
            if self.__s is not None:
                self.incrementStateActionPairFrequenceInN(self.__s, self.__a)
                self.insertActionValueInQ(self.__s, self.__a,
                                          self.getActionValueFromQ(self.__s, self.__a)
                                          + alpha * self.getStateActionPairFrequenceFromN(self.__s, self.__a)
                                          * (self.__r + gamma * self.maxActionValueForAllActionsInSPrime(
                                              sPrime) - self.getActionValueFromQ(self.__s, self.__a)))
            else:
                self.__s = TicTacToe(3)
            self.__s.initialize_game_matrix_with_another_game_matrix(sPrime)
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
        self.__DBCursor.execute(
            'CREATE TABLE IF NOT EXISTS N(ticTacToeStateHash INTEGER, actionInState TEXT, stateActionPairFrequence INTEGER)')

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
        maxActionValue = -999999
        allActionsInSPrime = sPrime.get_possible_moves()
        for action in allActionsInSPrime:
            maxActionValue = max(maxActionValue, self.getActionValueFromQ(sPrime, action))
        return maxActionValue

    def getMaxActionInStateFromQ(self, sPrime):
        ticTacToeStateHash = self.__zobristHash.get_hash(sPrime.game_matrix)
        self.__DBCursor.execute("SELECT * FROM Q WHERE ticTacToeStateHash = ?", [ticTacToeStateHash])
        listOfQEntries = self.__DBCursor.fetchall()
        if not len(listOfQEntries) > 0:
            self.maxActionValueForAllActionsInSPrime(sPrime)
            self.__DBCursor.execute("SELECT * FROM Q WHERE ticTacToeStateHash = ?", [ticTacToeStateHash])
            listOfQEntries = self.__DBCursor.fetchall()
        maxQEntry = max(listOfQEntries, key = itemgetter(2))
        return self.translateActionTupleString2IntTuple(str(maxQEntry[1]))

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

    def isStateActionPairInQ(self, ticTacToeStateHash, actionInState):
        self.__DBCursor.execute("SELECT * FROM Q WHERE ticTacToeStateHash = ? AND actionInState = ?",
                                [ticTacToeStateHash, actionInState])
        if len(self.__DBCursor.fetchall()) == 0:
            return False
        else:
            return True

    def closeDB(self):
        self.__DBCursor.close()
        self.__DBConnection.close()