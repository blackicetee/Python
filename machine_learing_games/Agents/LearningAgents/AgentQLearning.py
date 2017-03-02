import sqlite3


class AgentQLearning:
    def __init__(self):
        self.__ticTacToeDBCursor = None
        self.__ticTacToeDBConnection = None

    def learnTictactoe(self, gamesToPlay, TicTacToeDBName):
        pass

    def learnReversi(self, gamesToPlay, DBName):
        pass

    def suggestTicTacToeAction(self, tictactoeState):
        pass

    def suggestReversiAction(self, reversiState):
        pass

    def createTicTacToeDB(self, TicTacToeDBName):
        self.__ticTacToeDBConnection= sqlite3.connect(TicTacToeDBName)
        self.__ticTacToeDBCursor = self.__ticTacToeDBConnection.cursor()
        self.__ticTacToeDBCursor.execute('CREATE TABLE IF NOT EXISTS Q(ticTacToeStateHash INTEGER, ticTacToeAction INTEGER, ticTacToeActionValue REAL)')
        self.__ticTacToeDBCursor.execute('CREATE TABLE IF NOT EXISTS N(ticTacToeStateHash INTEGER, ticTacToeAction INTEGER, stateActionPairFrequence INTEGER)')

    def insertTicTacToeActionValueInQ(self, ticTacToeStateHash, ticTacToeAction, ticTacToeActionValue):
        if self.isTicTacToeStateActionInDB(ticTacToeStateHash, ticTacToeAction):
            self.__ticTacToeDBCursor.execute("UPDATE Q Set ticTacToeActionValue = ? WHERE ticTacToeStateHash = ? AND ticTacToeAction = ?",
                                    [ticTacToeActionValue, ticTacToeStateHash, ticTacToeAction])
        else:
            self.__ticTacToeDBCursor.execute("INSERT INTO Q(ticTacToeStateHash, ticTacToeAction, ticTacToeActionValue) VALUES (?, ?, ?)",
                (ticTacToeStateHash, ticTacToeAction, ticTacToeActionValue))
        self.__ticTacToeDBConnection.commit()

    def isTicTacToeStateActionInDB(self, ticTacToeStateHash, ticTacToeAction):
        self.__ticTacToeDBCursor.execute("SELECT * FROM Q WHERE ticTacToeStateHash = ? AND ticTacToeAction = ?", [ticTacToeStateHash, ticTacToeAction])
        if len(self.__ticTacToeDBCursor.fetchall()) == 0:
            return False
        else:
            return True

    def closeTicTacToeDB(self):
        self.__ticTacToeDBCursor.close()
        self.__ticTacToeDBConnection.close()

agent = AgentQLearning()

agent.createTicTacToeDB('ttt_db_1.db')
#agent.insertTicTacToeActionValueInQ(123456789, 12, 0.5)
#agent.insertTicTacToeActionValueInQ(123, 11, 0.0)
agent.insertTicTacToeActionValueInQ(541323567, 30, 0.23451234)
#agent.insertTicTacToeActionValueInQ(541323567, 30, 0.0)

agent.closeTicTacToeDB()