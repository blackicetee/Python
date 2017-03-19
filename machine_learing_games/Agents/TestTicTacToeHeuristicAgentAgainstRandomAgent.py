import unittest

from machine_learing_games.Agents import HeuristicSearchAgentTicTacToe
from machine_learing_games.Agents import RandomAgent
from machine_learing_games.tictactoe.TicTacToe import TicTacToe


class TestTicTacToeHeuristicAgentAgainstRandomAgentIn100TestGames(unittest.TestCase):
    def testAgainstFirstMoveRandomAgentIn9FieldTicTacToe(self):
        randomAgentWins = 0
        heuristicSearchAgentWins = 0
        for testGameCount in range(100):
            ttt = TicTacToe(3)
            while not ttt.is_terminal():
                RandomAgent.processTicTacToeAction(ttt)
                if not ttt.is_terminal():
                    HeuristicSearchAgentTicTacToe.processAction(ttt)
            print ttt.printable_game_matrix()
            if ttt.is_victory() and ttt.get_player_which_moved_last() == 'X':
                randomAgentWins += 1
            elif ttt.is_victory() and ttt.get_player_which_moved_last() == 'O':
                heuristicSearchAgentWins += 1
        print 'First Move random agent wins: ' + str(randomAgentWins) + ' games against heuristic search agent in 9 field Tic Tac Toe!'
        print 'Second Move heuristic search agent wins: ' + str(heuristicSearchAgentWins) + ' games against random agent in 9 field Tic Tac Toe!'
        self.assertTrue(heuristicSearchAgentWins >= 60)

    def testAgainstSecondMoveRandomAgentIn9FieldTicTacToe(self):
        randomAgentWins = 0
        heuristicSearchAgentWins = 0
        for testGameCount in range(100):
            ttt = TicTacToe(3)
            while not ttt.is_terminal():
                HeuristicSearchAgentTicTacToe.processAction(ttt)
                if not ttt.is_terminal():
                    RandomAgent.processTicTacToeAction(ttt)
            print ttt.printable_game_matrix()
            if ttt.is_victory() and ttt.get_player_which_moved_last() == 'X':
                heuristicSearchAgentWins += 1
            elif ttt.is_victory() and ttt.get_player_which_moved_last() == 'O':
                randomAgentWins += 1
        print 'Second Move random agent wins: ' + str(randomAgentWins) + ' games against heuristic search agent in 9 field Tic Tac Toe!'
        print 'First Move heuristic search agent wins: ' + str(heuristicSearchAgentWins) + ' games against random agent in 9 field Tic Tac Toe!'
        self.assertTrue(heuristicSearchAgentWins >= 60)

    def testAgainstFirstMoveRandomAgentIn16FieldTicTacToe(self):
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
        print 'First Move random agent wins: ' + str(
            randomAgentWins) + ' games against heuristic search agent in 16 field Tic Tac Toe!'
        print 'Second Move heuristic search agent wins: ' + str(
            heuristicSearchAgentWins) + ' games against random agent in 16 field Tic Tac Toe!'
        self.assertTrue(heuristicSearchAgentWins >= 60)

    def testAgainstSecondMoveRandomAgentIn16FieldTicTacToe(self):
        randomAgentWins = 0
        heuristicSearchAgentWins = 0
        for testGameCount in range(100):
            ttt = TicTacToe(4)
            while not ttt.is_terminal():
                HeuristicSearchAgentTicTacToe.processAction(ttt)
                if not ttt.is_terminal():
                    RandomAgent.processTicTacToeAction(ttt)
            print ttt.printable_game_matrix()
            if ttt.is_victory() and ttt.get_player_which_moved_last() == 'X':
                heuristicSearchAgentWins += 1
            elif ttt.is_victory() and ttt.get_player_which_moved_last() == 'O':
                randomAgentWins += 1
        print 'Second Move random agent wins: ' + str(
            randomAgentWins) + ' games against heuristic search agent in 9 field Tic Tac Toe!'
        print 'First Move heuristic search agent wins: ' + str(
            heuristicSearchAgentWins) + ' games against random agent in 9 field Tic Tac Toe!'
        self.assertTrue(heuristicSearchAgentWins >= 60)