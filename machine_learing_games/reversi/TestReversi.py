import unittest

import numpy as np

from machine_learing_games.reversi.Reversi import Reversi


class TestInitializeReversi(unittest.TestCase):
    def test_initialize_reversi_1(self):
        reversi = Reversi()


class TestSuggestMoves(unittest.TestCase):
    def test_suggest_horizontal_moves_right(self):
        reversi = Reversi()

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
        self.assertTrue((reversi.game_matrix == expected_game_matrix).all())

    def test_make_move_diagonal_bottom_left(self):
        expected_game_matrix = np.matrix([[' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                                          [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                                          [' ', ' ', 'B', 'W', ' ', 'W', ' ', ' '],
                                          [' ', ' ', ' ', 'B', 'W', 'B', ' ', ' '],
                                          [' ', ' ', 'B', 'W', 'B', ' ', ' ', ' '],
                                          [' ', ' ', 'W', ' ', ' ', ' ', ' ', ' '],
                                          [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                                          [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']])
        reversi = Reversi()
        reversi.make_move((3, 5))
        reversi.make_move((2, 3))
        reversi.make_move((2, 2))
        reversi.make_move((2, 5))
        reversi.make_move((4, 2))
        reversi.make_move((5, 2))
        self.assertTrue((reversi.game_matrix == expected_game_matrix).all())


    def test_make_move_horizontal_left_and_vertical_bottom(self):
        expected_game_matrix = np.matrix([[' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                                          [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                                          [' ', ' ', 'B', 'B', 'B', 'W', ' ', ' '],
                                          [' ', ' ', ' ', 'B', 'B', 'B', ' ', ' '],
                                          [' ', ' ', 'B', 'W', 'B', ' ', ' ', ' '],
                                          [' ', ' ', 'W', ' ', ' ', ' ', ' ', ' '],
                                          [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                                          [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']])
        reversi = Reversi()
        reversi.make_move((3, 5))
        reversi.make_move((2, 3))
        reversi.make_move((2, 2))
        reversi.make_move((2, 5))
        reversi.make_move((4, 2))
        reversi.make_move((5, 2))
        reversi.make_move((2, 4))
        self.assertTrue((reversi.game_matrix == expected_game_matrix).all())

    def test_make_move_diagonal_bottom_right(self):
        expected_game_matrix = np.matrix([[' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                                          [' ', ' ', ' ', 'W', ' ', ' ', ' ', ' '],
                                          [' ', ' ', 'B', 'W', 'W', 'W', ' ', ' '],
                                          [' ', ' ', 'B', 'B', 'B', 'W', ' ', ' '],
                                          [' ', ' ', 'B', 'W', 'B', ' ', 'W', ' '],
                                          [' ', ' ', 'W', ' ', ' ', ' ', ' ', ' '],
                                          [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                                          [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']])
        reversi = Reversi()
        reversi.make_move((3, 5))
        reversi.make_move((2, 3))
        reversi.make_move((2, 2))
        reversi.make_move((2, 5))
        reversi.make_move((4, 2))
        reversi.make_move((5, 2))
        reversi.make_move((2, 4))
        reversi.make_move((1, 3))
        reversi.make_move((3, 2))
        reversi.make_move((4, 6))
        self.assertTrue((reversi.game_matrix == expected_game_matrix).all())

    def test_make_move_complex_1(self):
        expected_game_matrix = np.matrix([[' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                                          [' ', ' ', ' ', 'W', ' ', ' ', ' ', ' '],
                                          [' ', ' ', 'B', 'B', 'B', 'B', 'B', ' '],
                                          [' ', ' ', 'B', 'B', 'B', 'B', ' ', ' '],
                                          [' ', ' ', 'B', 'W', 'B', ' ', 'W', ' '],
                                          [' ', ' ', 'W', ' ', ' ', ' ', ' ', ' '],
                                          [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                                          [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']])
        reversi = Reversi()
        reversi.make_move((3, 5))
        reversi.make_move((2, 3))
        reversi.make_move((2, 2))
        reversi.make_move((2, 5))
        reversi.make_move((4, 2))
        reversi.make_move((5, 2))
        reversi.make_move((2, 4))
        reversi.make_move((1, 3))
        reversi.make_move((3, 2))
        reversi.make_move((4, 6))
        reversi.make_move((2, 6))
        self.assertTrue((reversi.game_matrix == expected_game_matrix).all())

    def test_make_move_complex_2(self):
        expected_game_matrix = np.matrix([[' ', ' ', 'B', ' ', ' ', ' ', ' ', ' '],
                                          [' ', ' ', ' ', 'B', ' ', ' ', 'W', ' '],
                                          [' ', ' ', 'B', 'B', 'B', 'W', 'B', ' '],
                                          [' ', ' ', 'B', 'B', 'W', 'B', ' ', ' '],
                                          [' ', ' ', 'B', 'W', 'B', ' ', 'W', ' '],
                                          [' ', ' ', 'W', ' ', ' ', ' ', ' ', ' '],
                                          [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                                          [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']])
        reversi = Reversi()
        reversi.make_move((3, 5))
        reversi.make_move((2, 3))
        reversi.make_move((2, 2))
        reversi.make_move((2, 5))
        reversi.make_move((4, 2))
        reversi.make_move((5, 2))
        reversi.make_move((2, 4))
        reversi.make_move((1, 3))
        reversi.make_move((3, 2))
        reversi.make_move((4, 6))
        reversi.make_move((2, 6))
        reversi.make_move((1, 6))
        reversi.make_move((0, 0))
        reversi.make_move((1, 1))
        reversi.make_move((0, 2))
        self.assertTrue((reversi.game_matrix == expected_game_matrix).all())

    def test_make_move_complex_3(self):
        expected_game_matrix = np.matrix([[' ', ' ', 'B', ' ', ' ', ' ', ' ', ' '],
                                          [' ', ' ', ' ', 'B', ' ', 'B', 'W', ' '],
                                          [' ', 'W', 'B', 'W', 'B', 'B', 'B', ' '],
                                          ['W', 'W', 'W', 'B', 'W', 'B', ' ', ' '],
                                          [' ', ' ', 'B', 'W', 'B', ' ', 'W', ' '],
                                          [' ', ' ', 'W', ' ', ' ', ' ', ' ', ' '],
                                          [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                                          [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']])
        reversi = Reversi()
        reversi.make_move((3, 5))
        reversi.make_move((2, 3))
        reversi.make_move((2, 2))
        reversi.make_move((2, 5))
        reversi.make_move((4, 2))
        reversi.make_move((5, 2))
        reversi.make_move((2, 4))
        reversi.make_move((1, 3))
        reversi.make_move((3, 2))
        reversi.make_move((4, 6))
        reversi.make_move((2, 6))
        reversi.make_move((1, 6))
        reversi.make_move((0, 2))
        reversi.make_move((2, 1))
        reversi.make_move((3, 1))
        reversi.make_move((3, 0))
        reversi.make_move((1, 5))
        self.assertTrue((reversi.game_matrix == expected_game_matrix).all())

    def test_make_move_complex_4(self):
        expected_game_matrix = np.matrix([['B', ' ', 'B', ' ', 'B', ' ', ' ', 'B'],
                                          ['W', 'B', 'W', 'W', 'W', 'W', 'B', ' '],
                                          ['W', 'W', 'B', 'W', 'B', 'W', 'B', ' '],
                                          ['W', 'B', 'W', 'B', 'W', 'B', 'B', 'B'],
                                          [' ', ' ', 'B', 'W', 'B', 'B', 'B', 'B'],
                                          [' ', 'W', 'W', 'W', 'W', 'B', 'B', 'B'],
                                          [' ', ' ', ' ', ' ', ' ', ' ', ' ', 'B'],
                                          [' ', ' ', ' ', ' ', ' ', ' ', ' ', 'B']])
        reversi = Reversi()
        reversi.make_move((3, 5))
        reversi.make_move((2, 3))
        reversi.make_move((2, 2))
        reversi.make_move((2, 5))

        reversi.make_move((4, 2))
        reversi.make_move((5, 2))
        reversi.make_move((2, 4))
        reversi.make_move((1, 3))

        reversi.make_move((3, 2))
        reversi.make_move((4, 6))
        reversi.make_move((2, 6))
        reversi.make_move((1, 6))

        reversi.make_move((0, 2))
        reversi.make_move((2, 1))
        reversi.make_move((3, 1))
        reversi.make_move((3, 0))

        reversi.make_move((1, 5))
        reversi.make_move((3, 6))
        reversi.make_move((5, 7))
        reversi.make_move((1, 4))

        reversi.make_move((0, 4))
        reversi.make_move((4, 5))
        reversi.make_move((3, 7))
        reversi.make_move((1, 2))

        reversi.make_move((0, 7))
        reversi.make_move((5, 1))
        reversi.make_move((2, 0))
        reversi.make_move((1, 1))

        reversi.make_move((5, 3))
        reversi.make_move((1, 0))
        reversi.make_move((0, 0))
        reversi.make_move((4, 7))

        reversi.make_move((5, 6))
        reversi.make_move((6, 7))
        reversi.make_move((7, 7))
        reversi.make_move((5, 4))

        reversi.make_move((5, 5))
        reversi.make_move((6, 7))
        reversi.make_move((7, 7))
        reversi.make_move((5, 4))

        print reversi.printable_game_matrix()
        self.assertTrue((reversi.game_matrix == expected_game_matrix).all())