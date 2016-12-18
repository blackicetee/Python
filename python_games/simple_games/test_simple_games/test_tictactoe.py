import unittest
from numpy import matrix
from numpy import shape
import numpy

from python_games.simple_games.TicTacToe import TicTacToe


class TestInitializeTicTacToe(unittest.TestCase):
    """Tests if the matrix shape of an initialized
    TicTacToe game is correct."""

    def test_initialize_4x4_TicTacToe_matrix(self):
        ttt_4x4 = TicTacToe(4, 4)
        self.assertEqual((4, 4), shape(ttt_4x4.game_matrix))

    def test_initialize_8x8_TicTacToe_matrix(self):
        ttt_8x8 = TicTacToe(8, 8)
        self.assertEqual((8, 8), shape(ttt_8x8.game_matrix))


class TestTranslateGameTokenType(unittest.TestCase):
    """Tests if game token type is translated correctly into predefined
    float values or otherwise a value error exception is raced."""

    def setUp(self):
        self.ticTacToe = TicTacToe(4, 4)

    def test_translate_game_token_O(self):
        self.assertEqual(1.0, self.ticTacToe.translate_game_token_type('O'))

    def test_translate_game_token_X(self):
        self.assertEqual(2.0, self.ticTacToe.translate_game_token_type('X'))

    def test_translate_game_token_invalid_number(self):
        self.assertRaises(ValueError, self.ticTacToe.translate_game_token_type, 8)

    def test_translate_game_token_invalid_character(self):
        self.assertRaises(ValueError, self.ticTacToe.translate_game_token_type, 'c')


class TestIsPositionFree(unittest.TestCase):
    """Tests if a position inside the game matrix is free so equals 0.0"""

    def setUp(self):
        self.ticTacToe = TicTacToe(4, 4)
        self.ticTacToe.put_game_token('X', (0, 1))

    def test_position_is_free(self):
        self.assertTrue(self.ticTacToe.is_position_free((0, 0)))

    def test_position_is_not_free(self):
        self.assertFalse(self.ticTacToe.is_position_free((0, 1)))

    def test_position_is_outside_of_matrix(self):
        self.assertRaises(ValueError, self.ticTacToe.is_position_free, (4, 4))


class TestPutGameToken(unittest.TestCase):
    """"""

    def setUp(self):
        self.ticTacToe = TicTacToe(4, 4)

    def test_fill_game_matrix_with_twos(self):
        for row in range(4):
            for col in range(4):
                self.ticTacToe.put_game_token('X', (row, col))

        matrix_filled_with_twos = \
            matrix([[2.0, 2.0, 2.0, 2.0],
                    [2.0, 2.0, 2.0, 2.0],
                    [2.0, 2.0, 2.0, 2.0],
                    [2.0, 2.0, 2.0, 2.0]])

        equality_matrix = matrix_filled_with_twos == self.ticTacToe.game_matrix
        self.assertTrue(equality_matrix.all())


def suite():
    """Returns an aggregation(called test suite)
    of all test cases in this test module"""
    suite1 = unittest.TestLoader().loadTestsFromTestCase(TestInitializeTicTacToe)
    suite2 = unittest.TestLoader().loadTestsFromTestCase(TestTranslateGameTokenType)
    suite3 = unittest.TestLoader().loadTestsFromTestCase(TestIsPositionFree)
    suite4 = unittest.TestLoader().loadTestsFromTestCase(TestPutGameToken)
    return unittest.TestSuite([suite1, suite2, suite3, suite4])
