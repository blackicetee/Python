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
        self.example_ticTacToe_game = TicTacToe(4, 4)
        self.example_ticTacToe_game.put_game_token('X', (0, 0))
        self.example_ticTacToe_game.put_game_token('O', (3, 3))
        self.example_ticTacToe_game.put_game_token('X', (0, 1))
        self.example_ticTacToe_game.put_game_token('O', (2, 2))
        self.example_ticTacToe_game.put_game_token('X', (0, 2))
        self.example_ticTacToe_game.put_game_token('O', (1, 1))
        self.example_ticTacToe_game.put_game_token('X', (0, 3))

    def test_put_seven_game_tokens(self):
        self.ticTacToe.put_game_token('X', (0, 0))
        self.ticTacToe.put_game_token('O', (3, 3))
        self.ticTacToe.put_game_token('X', (0, 1))
        self.ticTacToe.put_game_token('O', (2, 2))
        self.ticTacToe.put_game_token('X', (0, 2))
        self.ticTacToe.put_game_token('O', (1, 1))
        self.ticTacToe.put_game_token('X', (0, 3))
        equality_matrix = self.example_ticTacToe_game.game_matrix == self.ticTacToe.game_matrix
        self.assertTrue(equality_matrix.all())

    def test_if_value_not_changes_when_position_is_taken(self):
        copy_example_ticTacToe_game = self.example_ticTacToe_game
        copy_example_ticTacToe_game.put_game_token('X', (0, 0))
        copy_example_ticTacToe_game.put_game_token('O', (3, 3))
        copy_example_ticTacToe_game.put_game_token('O', (0, 1))
        copy_example_ticTacToe_game.put_game_token('X', (2, 2))
        self.assertTrue((copy_example_ticTacToe_game.game_matrix == self.example_ticTacToe_game.game_matrix).all())

    def test_return_value_by_empty_position(self):
        self.assertTrue(self.ticTacToe.put_game_token('X', (1, 1)))

    def test_return_value_by_taken_position(self):
        self.ticTacToe.put_game_token('X', (1, 1))
        self.assertFalse(self.ticTacToe.put_game_token('X', (1, 1)))


class TestResetGameMatrix(unittest.TestCase):
    def test_reset_game_matrix(self):
        example_ticTacToe_game = TicTacToe(4, 4)
        example_ticTacToe_game.put_game_token('X', (0, 0))
        example_ticTacToe_game.put_game_token('O', (3, 3))
        example_ticTacToe_game.put_game_token('X', (0, 1))
        example_ticTacToe_game.put_game_token('O', (2, 2))
        example_ticTacToe_game.put_game_token('X', (0, 2))
        example_ticTacToe_game.put_game_token('O', (1, 1))
        example_ticTacToe_game.put_game_token('X', (0, 3))
        example_ticTacToe_game.reset_game_matrix_values()
        test_ticTacToe = TicTacToe(4, 4)
        self.assertTrue((test_ticTacToe.game_matrix == example_ticTacToe_game.game_matrix).all())


class TestHorizontalVictory(unittest.TestCase):

    def setUp(self):
        self.example_ticTacToe_game = TicTacToe(4, 4)
        self.example_ticTacToe_game.put_game_token('X', (2, 0))
        self.example_ticTacToe_game.put_game_token('O', (3, 3))
        self.example_ticTacToe_game.put_game_token('X', (2, 1))
        self.example_ticTacToe_game.put_game_token('O', (1, 1))
        self.example_ticTacToe_game.put_game_token('X', (2, 2))
        self.example_ticTacToe_game.put_game_token('O', (0, 0))

    def test_horizontal_victory(self):
        self.example_ticTacToe_game.put_game_token('X', (2, 3))
        self.assertTrue(self.example_ticTacToe_game.is_horizontal_victory())

    def test_no_horizontal_victory(self):
        self.assertFalse(self.example_ticTacToe_game.is_horizontal_victory())


class TestVerticalVictory(unittest.TestCase):

    def setUp(self):
        self.example_ticTacToe_game = TicTacToe(4, 4)
        self.example_ticTacToe_game.put_game_token('X', (0, 0))
        self.example_ticTacToe_game.put_game_token('O', (3, 3))
        self.example_ticTacToe_game.put_game_token('X', (1, 0))
        self.example_ticTacToe_game.put_game_token('O', (2, 3))
        self.example_ticTacToe_game.put_game_token('X', (2, 0))
        self.example_ticTacToe_game.put_game_token('O', (1, 3))

    def test_vertical_victory(self):
        self.example_ticTacToe_game.put_game_token('X', (3, 0))
        self.assertTrue(self.example_ticTacToe_game.is_vertical_victory())

    def test_no_vertical_victory(self):
        self.assertFalse(self.example_ticTacToe_game.is_vertical_victory())

class TestDiagonalVictory(unittest.TestCase):
    def setUp(self):
        self.example_ticTacToe_game = TicTacToe(4, 4)
        self.example_ticTacToe_game.put_game_token('X', (0, 0))
        self.example_ticTacToe_game.put_game_token('O', (3, 0))
        self.example_ticTacToe_game.put_game_token('X', (1, 1))
        self.example_ticTacToe_game.put_game_token('O', (3, 1))
        self.example_ticTacToe_game.put_game_token('X', (2, 2))
        self.example_ticTacToe_game.put_game_token('O', (3, 2))

    def test_diagonal_victory_top_left_to_bottom_right(self):
        self.example_ticTacToe_game.put_game_token('X', (3, 3))
        self.assertTrue(self.example_ticTacToe_game.is_diagonal_victory())

    def test_digital_victory_top_right_to_bottom_left(self):
        example_tictactoe = TicTacToe(4, 4)
        example_tictactoe.put_game_token('X', (0, 3))
        example_tictactoe.put_game_token('O', (0, 0))
        example_tictactoe.put_game_token('X', (1, 2))
        example_tictactoe.put_game_token('O', (1, 0))
        example_tictactoe.put_game_token('X', (2, 1))
        example_tictactoe.put_game_token('O', (2, 0))
        example_tictactoe.put_game_token('X', (3, 0))
        self.assertTrue(example_tictactoe.is_diagonal_victory())

    def test_no_digital_victory(self):
        self.assertFalse(self.example_ticTacToe_game.is_vertical_victory())


def suite():
    """Returns an aggregation(called test suite)
    of all test cases in this test module"""
    suite1 = unittest.TestLoader().loadTestsFromTestCase(TestInitializeTicTacToe)
    suite2 = unittest.TestLoader().loadTestsFromTestCase(TestTranslateGameTokenType)
    suite3 = unittest.TestLoader().loadTestsFromTestCase(TestIsPositionFree)
    suite4 = unittest.TestLoader().loadTestsFromTestCase(TestPutGameToken)
    suite5 = unittest.TestLoader().loadTestsFromTestCase(TestResetGameMatrix)
    suite6 = unittest.TestLoader().loadTestsFromTestCase(TestHorizontalVictory)
    suite7 = unittest.TestLoader().loadTestsFromTestCase(TestVerticalVictory)
    suite8 = unittest.TestLoader().loadTestsFromTestCase(TestDiagonalVictory)
    return unittest.TestSuite([suite1, suite2, suite3, suite4, suite5, suite6, suite7, suite8])
