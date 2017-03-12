import unittest

from machine_learing_games.Agents import HeuristicSearchAgentReversi
from machine_learing_games.Agents import HeuristicSearchAgentTicTacToe
from machine_learing_games.Agents import RandomAgent
from machine_learing_games.Agents.LearningAgents.TicTacToeTDQLearningAgent import TicTacToeTDQLearningAgent, \
    TICTACTOE_3x3_TDQ_AGENT_100_NAME, TICTACTOE_3x3_TDQ_AGENT_1000_NAME, TICTACTOE_3x3_TDQ_AGENT_10000_NAME
from machine_learing_games.Reversi.Reversi import Reversi
from machine_learing_games.tictactoe.TicTacToe import TicTacToe


class TestTicTacToeHeuristic(unittest.TestCase):
    def test100GamesAgainstRandomAgentX(self):
        randomAgentWins = 0
        heuristicSearchAgentWins = 0
        for testGameCount in range(100):
            ttt = TicTacToe(4)
            while not ttt.is_terminal():
                RandomAgent.processTicTacToeAction(ttt)
                if not ttt.is_terminal():
                    HeuristicSearchAgentTicTacToe.processAction(ttt)
            print ttt.printable_game_matrix()
            if ttt.is_victory() and ttt.get_player_which_moved_last() == 'X':
                randomAgentWins += 1
            elif ttt.is_victory() and ttt.get_player_which_moved_last() == 'O':
                heuristicSearchAgentWins += 1
        print 'Random agent wins:' + str(randomAgentWins) + 'games against heuristic search agent in Tic Tac Toe!'
        print 'Heuristic search agent Tic Tac Toe wins:' + str(heuristicSearchAgentWins) + 'games against random agent!'
        self.assertTrue(heuristicSearchAgentWins > 50)

class TestReversiHeuristic(unittest.TestCase):
    def test100GamesAgainstRandomAgentBlack(self):
        randomAgentWins = 0
        reversiHeuristicSearchAgentWins = 0
        for testGameCount in range(5):
            reversi = Reversi()
            while not reversi.is_victory():
                if reversi.player_to_move() == 'B':
                    RandomAgent.processReversiAction(reversi)
                if reversi.player_to_move() == 'W' and not reversi.is_victory():
                    HeuristicSearchAgentReversi.processAction(reversi)
            print reversi.printable_game_matrix()
            print 'Black token count is: ' + str(reversi.count_all_black_tokens())
            print 'White token count is: ' + str(reversi.count_all_white_tokens())
            if reversi.is_victory() and reversi.count_all_black_tokens() > reversi.count_all_white_tokens():
                randomAgentWins += 1
            elif reversi.is_victory() and reversi.count_all_black_tokens() < reversi.count_all_white_tokens():
                reversiHeuristicSearchAgentWins += 1
        print 'Random agent wins: ' + str(randomAgentWins) + ' games against heuristic search agent in reversi!'
        print 'Heuristic search agent reversi wins: ' + str(reversiHeuristicSearchAgentWins) + ' games against random agent!'

class Test9FieldTicTacToeTDQLearnAgent(unittest.TestCase):
    def testsTDQLearnAgent100AgainstFirstMoveRandomAgentIn100TestGames(self):
        randomAgentWins = 0
        TDQLearnAgentWins = 0
        agent = TicTacToeTDQLearningAgent(TICTACTOE_3x3_TDQ_AGENT_100_NAME, 3)
        for testGameCount in range(100):
            ttt = TicTacToe(3)
            while not ttt.is_terminal():
                RandomAgent.processTicTacToeAction(ttt)
                if not ttt.is_terminal():
                    TDQAction = agent.suggestAction(ttt)
                    ttt.make_move(TDQAction)
            print ttt.printable_game_matrix()
            if ttt.is_victory() and ttt.get_player_which_moved_last() == 'X':
                randomAgentWins += 1
            elif ttt.is_victory() and ttt.get_player_which_moved_last() == 'O':
                TDQLearnAgentWins += 1
        print 'Random agent wins:' + str(randomAgentWins) + 'games against TD-Q-Learn Agent100 in Tic Tac Toe!'
        print 'TD-Q-LearnTrained100Games agent wins:' + str(TDQLearnAgentWins) + ' Tic Tac Toe  games against random agent!'
        self.assertTrue(TDQLearnAgentWins > 50)

    def testsTDQLearnAgent100AgainstSecondMoveRandomAgentIn100TestGames(self):
        randomAgentWins = 0
        TDQLearnAgentWins = 0
        agent = TicTacToeTDQLearningAgent(TICTACTOE_3x3_TDQ_AGENT_100_NAME, 3)
        for testGameCount in range(100):
            ttt = TicTacToe(3)
            while not ttt.is_terminal():
                TDQAction = agent.suggestAction(ttt)
                ttt.make_move(TDQAction)
                if not ttt.is_terminal():
                    RandomAgent.processTicTacToeAction(ttt)
            print ttt.printable_game_matrix()
            if ttt.is_victory() and ttt.get_player_which_moved_last() == 'X':
                TDQLearnAgentWins+= 1
            elif ttt.is_victory() and ttt.get_player_which_moved_last() == 'O':
                randomAgentWins += 1
        print 'Random agent wins:' + str(randomAgentWins) + 'games against TD-Q-Learn Agent100 in Tic Tac Toe!'
        print 'TD-Q-LearnTrained100Games agent wins:' + str(TDQLearnAgentWins) + ' Tic Tac Toe  games against random agent!'
        self.assertTrue(TDQLearnAgentWins > 50)

    def testsTDQLearnAgent1000AgainstFirstMoveRandomAgentIn100TestGames(self):
        randomAgentWins = 0
        TDQLearnAgentWins = 0
        agent = TicTacToeTDQLearningAgent(TICTACTOE_3x3_TDQ_AGENT_1000_NAME, 3)
        for testGameCount in range(100):
            ttt = TicTacToe(3)
            while not ttt.is_terminal():
                RandomAgent.processTicTacToeAction(ttt)
                if not ttt.is_terminal():
                    TDQAction = agent.suggestAction(ttt)
                    ttt.make_move(TDQAction)
            print ttt.printable_game_matrix()
            if ttt.is_victory() and ttt.get_player_which_moved_last() == 'X':
                randomAgentWins += 1
            elif ttt.is_victory() and ttt.get_player_which_moved_last() == 'O':
                TDQLearnAgentWins += 1
        print 'Random agent wins: ' + str(randomAgentWins) + ' games against TD-Q-Learn Agent1000 in Tic Tac Toe!'
        print 'TD-Q-LearnTrained1000Games agent wins: ' + str(TDQLearnAgentWins) + ' Tic Tac Toe  games against random agent!'
        self.assertTrue(TDQLearnAgentWins > 50)

    def testsTDQLearnAgent1000AgainstSecondMoveRandomAgentIn100TestGames(self):
        randomAgentWins = 0
        TDQLearnAgentWins = 0
        agent = TicTacToeTDQLearningAgent(TICTACTOE_3x3_TDQ_AGENT_1000_NAME, 3)
        for testGameCount in range(100):
            ttt = TicTacToe(3)
            while not ttt.is_terminal():
                TDQAction = agent.suggestAction(ttt)
                ttt.make_move(TDQAction)
                if not ttt.is_terminal():
                    RandomAgent.processTicTacToeAction(ttt)
            print ttt.printable_game_matrix()
            if ttt.is_victory() and ttt.get_player_which_moved_last() == 'X':
                TDQLearnAgentWins += 1
            elif ttt.is_victory() and ttt.get_player_which_moved_last() == 'O':
                randomAgentWins += 1
        print 'Random agent wins: ' + str(randomAgentWins) + ' games against TD-Q-Learn Agent1000 in Tic Tac Toe!'
        print 'TD-Q-LearnTrained1000Games agent wins: ' + str(TDQLearnAgentWins) + ' Tic Tac Toe  games against random agent!'
        self.assertTrue(TDQLearnAgentWins > 50)


    def testsTDQLearnAgent10000AgainstFirstMoveRandomAgentIn100TestGames(self):
        randomAgentWins = 0
        TDQLearnAgentWins = 0
        agent = TicTacToeTDQLearningAgent(TICTACTOE_3x3_TDQ_AGENT_10000_NAME, 3)
        for testGameCount in range(100):
            ttt = TicTacToe(3)
            while not ttt.is_terminal():
                RandomAgent.processTicTacToeAction(ttt)
                if not ttt.is_terminal():
                    TDQAction = agent.suggestAction(ttt)
                    ttt.make_move(TDQAction)
            print ttt.printable_game_matrix()
            if ttt.is_victory() and ttt.get_player_which_moved_last() == 'X':
                randomAgentWins += 1
            elif ttt.is_victory() and ttt.get_player_which_moved_last() == 'O':
                TDQLearnAgentWins += 1
        print 'Random agent wins: ' + str(randomAgentWins) + ' games against TD-Q-Learn Agent1000 in Tic Tac Toe!'
        print 'TD-Q-LearnTrained1000Games agent wins: ' + str(
            TDQLearnAgentWins) + ' Tic Tac Toe  games against random agent!'
        self.assertTrue(TDQLearnAgentWins > 50)


    def testsTDQLearnAgent10000AgainstSecondMoveRandomAgentIn100TestGames(self):
        randomAgentWins = 0
        TDQLearnAgentWins = 0
        agent = TicTacToeTDQLearningAgent(TICTACTOE_3x3_TDQ_AGENT_10000_NAME, 3)
        for testGameCount in range(100):
            ttt = TicTacToe(3)
            while not ttt.is_terminal():
                TDQAction = agent.suggestAction(ttt)
                ttt.make_move(TDQAction)
                if not ttt.is_terminal():
                    RandomAgent.processTicTacToeAction(ttt)
            print ttt.printable_game_matrix()
            if ttt.is_victory() and ttt.get_player_which_moved_last() == 'X':
                TDQLearnAgentWins += 1
            elif ttt.is_victory() and ttt.get_player_which_moved_last() == 'O':
                randomAgentWins += 1
        print 'Random agent wins: ' + str(randomAgentWins) + ' games against TD-Q-Learn Agent1000 in Tic Tac Toe!'
        print 'TD-Q-LearnTrained1000Games agent wins: ' + str(
            TDQLearnAgentWins) + ' Tic Tac Toe  games against random agent!'
        self.assertTrue(TDQLearnAgentWins > 50)


