import unittest

import numpy as np

from machine_learing_games.reversi.Reversi import Reversi


class TestInitializeReversi(unittest.TestCase):
    def test_initialize_reversi_1(self):
        reversi = Reversi()
        print reversi.printable_game_matrix()
        print reversi.suggest_moves()
        reversi.make_move((3,5))
        print reversi.printable_game_matrix()


class TestSuggestMoves(unittest.TestCase):
    def test_suggest_horizontal_moves_right(self):
        reversi = Reversi()
        print reversi.printable_game_matrix()
        print reversi.suggest_horizontal_moves()
        print reversi.suggest_vertical_moves()
        print "Get all token positions: " + str(reversi.get_all_token_positions(reversi.get_player_to_move()))

class TestMakeMoves(unittest.TestCase):
    def test_make_move_horizontal_right_and_vertical_top(self):
        expected_game_matrix = np.matrix([[' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                                          [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                                          [' ', ' ', ' ', 'W', ' ', ' ', ' ', ' '],
                                          [' ', ' ', ' ', 'W', 'B', 'B', ' ', ' '],
                                          [' ', ' ', ' ', 'W', 'B', ' ', ' ', ' '],
                                          [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                                          [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                                          [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']])
        reversi = Reversi()
        reversi.make_move((3, 5))
        reversi.make_move((2, 3))
        self.assertTrue((reversi.game_matrix == expected_game_matrix).all())

    def test_make_move_diagonal_top_left(self):
        expected_game_matrix = np.matrix([[' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                                          [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                                          [' ', ' ', 'B', 'W', ' ', ' ', ' ', ' '],
                                          [' ', ' ', ' ', 'B', 'B', 'B', ' ', ' '],
                                          [' ', ' ', ' ', 'W', 'B', ' ', ' ', ' '],
                                          [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                                          [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                                          [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']])
        reversi = Reversi()
        reversi.make_move((3, 5))
        reversi.make_move((2, 3))
        reversi.make_move((2, 2))
        print reversi.printable_game_matrix()
        self.assertTrue((reversi.game_matrix == expected_game_matrix).all())

    def test_make_move_diagonal_top_right(self):
        expected_game_matrix = np.matrix([[' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                                          [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                                          [' ', ' ', 'B', 'W', ' ', 'W', ' ', ' '],
                                          [' ', ' ', ' ', 'B', 'W', 'B', ' ', ' '],
                                          [' ', ' ', ' ', 'W', 'B', ' ', ' ', ' '],
                                          [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                                          [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                                          [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']])
        reversi = Reversi()
        reversi.make_move((3, 5))
        reversi.make_move((2, 3))
        reversi.make_move((2, 2))
        reversi.make_move((2, 5))
        print reversi.suggest_moves()
        print reversi.printable_game_matrix()
        self.assertTrue((reversi.game_matrix == expected_game_matrix).all())