import sqlite3
from operator import itemgetter

import logging

from machine_learing_games.Agents import RandomAgent
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
        self.__count_of_trained_games = 0
        self.__zobristHash = TicTacToeZobrist()
        self.__zobristHash.set_zobrist_board_positoin_array(TicTacToeZobrist().getFixed9FieldTicTacToeZobristBoardPositionArray())


    def learnTictactoe(self, gamesToPlay):
        for gameCount in range(gamesToPlay):
            ttt = TicTacToe(3)
            logging.info('Learning against itself game: ' + str(gameCount))
            while not ttt.is_terminal():
                qAction = self.qLearnIteration(ttt, self.R(ttt), 0.1, 1)
                logging.info('\n' + ttt.printable_game_matrix())
                logging.info(self.__zobristHash.get_hash(ttt.game_matrix))
                logging.info(qAction)
                ttt.make_move(qAction)
            if ttt.is_terminal():
                self.qLearnIteration(ttt, self.R(ttt), 0.1, 1)
            self.__s = None
            self.__a = None
            self.__r = None

    def suggestAction(self, state):
        return self.getMaxActionInStateFromQ(state)

    def exporationStrategyTicTacToe(self):
        ttt = TicTacToe(3)
        while not ttt.is_terminal():
            pass

    #https://www.youtube.com/watch?v=1XRahNzA5bE
    # with N Table
    def qLearnIteration(self, sPrime, rPrime, alpha, gamma):
        if self.isTerminal(sPrime):
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
            self.__a = self.getMaxActionInStateFromQ(sPrime)
            self.__r = rPrime
            return self.__a

    def player(self, s):
        if s.count_of_game_tokens_in_game() % 2 == 0:
            return 'X'
        elif s.count_of_game_tokens_in_game() % 2 == 1:
            return 'O'

    def R(self, s):
        if self.player(s) == 'X' and s.is_victory():
            return -1
        elif self.player(s) != 'X' and s.is_victory():
            return 1
        elif s.count_of_game_tokens_in_game() == s.get_maximal_amount_of_game_tokens() and not s.is_victory():
            return 0.2
        else:
            return -0.04

    def U(self, s):
        return self.getMaxActionInStateFromQ(s)

    def isTerminal(self, s):
        if s.is_victory():
            return True
        elif not s.is_victory() and s.count_of_game_tokens_in_game() == s.get_maximal_amount_of_game_tokens():
            return True
        else:
            return False


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
