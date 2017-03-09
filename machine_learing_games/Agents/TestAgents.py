import unittest

from machine_learing_games.Agents import HeuristicSearchAgentReversi
from machine_learing_games.Agents import HeuristicSearchAgentTicTacToe
from machine_learing_games.Agents import RandomAgent
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
        for testGameCount in range(1):
            reversi = Reversi()
            while not reversi.is_victory():
                RandomAgent.processReversiAction(reversi)
                if not reversi.is_victory():
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


