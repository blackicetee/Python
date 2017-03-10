import unittest

from machine_learing_games.Agents import HeuristicSearchAgentReversi
from machine_learing_games.Agents import HeuristicSearchAgentTicTacToe
from machine_learing_games.Agents import RandomAgent
from machine_learing_games.Agents.LearningAgents.TicTacToeTDQLearningAgent import TDQLearningAgentTicTacToe
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
    def testsTDQLearnAgent100AgainstRandomAgentIn100TestGames(self):
        randomAgentWins = 0
        TDQLearnAgentWins = 0
        agent = TDQLearningAgentTicTacToe('3x3_ttt_tdq_agent_100_.db')
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
        print 'Random agent wins:' + str(randomAgentWins) + 'games against TD-Q-Learn Agent in Tic Tac Toe!'
        print 'TD-Q-LearnTrained100Games agent wins:' + str(TDQLearnAgentWins) + ' Tic Tac Toe  games against random agent!'
        self.assertTrue(TDQLearnAgentWins > 50)

    def testsTDQLearnAgent1000AgainstRandomAgentIn100TestGames(self):
        randomAgentWins = 0
        TDQLearnAgentWins = 0
        agent = TDQLearningAgentTicTacToe('3x3_ttt_tdq_agent_1000_.db')
        for testGameCount in range(1000):
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
        print 'Random agent wins:' + str(randomAgentWins) + 'games against TD-Q-Learn Agent in Tic Tac Toe!'
        print 'TD-Q-LearnTrained100Games agent wins:' + str(TDQLearnAgentWins) + ' Tic Tac Toe  games against random agent!'
        self.assertTrue(TDQLearnAgentWins > 50)


