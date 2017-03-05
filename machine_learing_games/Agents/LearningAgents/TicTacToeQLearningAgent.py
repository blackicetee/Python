import sqlite3
from operator import itemgetter
from machine_learing_games.Agents import RandomAgent
from machine_learing_games.tictactoe.TicTacToe import TicTacToe
from machine_learing_games.tictactoe.TicTacToeZobrist import TicTacToeZobrist


class TicTacToeQLearningAgent:
    def __init__(self, TicTacToeDBName):
        self.__DBCursor = None
        self.__DBConnection = None
        self.createDB(TicTacToeDBName)
        self.__s = None
        self.__a = None
        self.__r = None
        self.__zobristHash = TicTacToeZobrist()

    def learnTictactoe(self, gamesToPlay):
        pass

    def suggestAction(self, state):
        pass

    #https://www.youtube.com/watch?v=1XRahNzA5bE
    def qLearnIteration(self, sPrime, rPrime, alpha, gamma):
        if self.__s is not None:
            if self.isTerminal(self.__s):
                self.insertActionValueInQ(self.__zobristHash.get_hash(self.__s.game_matrix), None, rPrime)
            else:
                self.incrementStateActionPairFrequenceInN(self.__s, self.__a)
                self.insertActionValueInQ(self.__s, self.__a,
                                          self.getActionValueFromQ(self.__s, self.__a)
                                          + alpha * self.getStateActionPairFrequenceFromN(self.__s, self.__a)
                                          * (self.__r + gamma * self.maxActionValueForAllActionsInSPrime(sPrime) - self.getActionValueFromQ(self.__s, self.__a)))
        self.__s = sPrime
        self.__a = self.maxActionValueForAllActionsInSPrime(sPrime)
        self.__r = rPrime

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
            return 0

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

    def insertActionValueInQ(self, ticTacToeStateHash, actionInState, actionValue):
        actionInState = str(actionInState)
        if self.isStateActionPairInQ(ticTacToeStateHash, actionInState):
            self.__DBCursor.execute("UPDATE Q Set actionValue = ? WHERE ticTacToeStateHash = ? AND actionInState = ?",
                                    [actionValue, ticTacToeStateHash, actionInState])
        else:
            self.__DBCursor.execute("INSERT INTO Q(ticTacToeStateHash, actionInState, actionValue) VALUES (?, ?, ?)",
                                    (ticTacToeStateHash, actionInState, actionValue))
        self.__DBConnection.commit()

    def getActionValueFromQ(self, ticTacToeStateHash, actionInState):
        self.__DBCursor.execute(
            "SELECT actionValue FROM Q WHERE ticTacToeStateHash = ? AND actionInState = ?",
            [ticTacToeStateHash, actionInState])
        results = self.__DBCursor.fetchall()
        if len(results) > 0:
            return results[0][0]
        else:
            self.insertActionValueInQ(ticTacToeStateHash, actionInState, 0)
            return 0

    def maxActionValueForAllActionsInSPrime(self, sPrime):
        maxActionValue = -999999
        allActionsInSPrime = sPrime.get_possible_moves()
        for action in allActionsInSPrime:
            sPrime.make_move(action)
            zobristHash = self.__zobristHash.get_hash(sPrime.game_matrix)
            maxActionValue = max(maxActionValue, self.getActionValueFromQ(zobristHash, action))
            sPrime.undo_move()
        return maxActionValue

    def getMaxActionInStateFromQ(self, ticTacToeStateHash):
        self.__DBCursor.execute("SELECT * FROM Q WHERE ticTacToeStateHash = ?", [ticTacToeStateHash])
        listOfQEntries = self.__DBCursor.fetchall()
        maxQEntry = max(listOfQEntries, key = itemgetter(2))
        return self.translateActionTupleString2IntTuple(str(maxQEntry[1]))

    def getMaxActionValueFromQ(self, ticTacToeStateHash):
        self.__DBCursor.execute("SELECT * FROM Q WHERE ticTacToeStateHash = ?", [ticTacToeStateHash])
        listOfQEntries = self.__DBCursor.fetchall()
        maxQEntry = max(listOfQEntries, key = itemgetter(2))
        return self.translateActionTupleString2IntTuple(maxQEntry[2])

    def translateActionTupleString2IntTuple(self, stringActionTuple):
        tupleStringValues = stringActionTuple.translate(None, '( )').split(',')
        return (int(tupleStringValues[0]), int(tupleStringValues[1]))

    def incrementStateActionPairFrequenceInN(self, ticTacToeStateHash, actionInState):
        stateActionPairFrequence = self.getStateActionPairFrequenceFromN(ticTacToeStateHash, actionInState)
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

    def getStateActionPairFrequenceFromN(self, ticTacToeStateHash, actionInState):
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


agent = TicTacToeQLearningAgent('ttt_db_1.db')
# agent.insertActionValueInQ(123, (0, 0), 0.0)
# agent.insertActionValueInQ(123, (0, 1), 0.0)
# agent.insertActionValueInQ(123, (0, 2), 0.2)
# agent.insertActionValueInQ(123, (0, 3), 0.7)
# agent.insertActionValueInQ(123, (3, 3), 0.7)
# agent.insertActionValueInQ(123, (1, 2), 0.0)
# agent.insertActionValueInQ(123, (1, 3), 0.2)
# agent.insertActionValueInQ(123, (2, 0), -0.2)
# print agent.getMaxActionInStateFromQ(123)
for i in range(1000):
    ttt = RandomAgent.getRandomNonTerminalTicTacToeState()
    # print ttt.printable_game_matrix()
    print agent.maxActionValueForAllActionsInSPrime(ttt)
agent.closeDB()
