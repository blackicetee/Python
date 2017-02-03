import unittest

import numpy as np

from machine_learing_games.tictactoe.TicTacToe import TicTacToe


class TestInitializeTicTacToe(unittest.TestCase):
    def test_initialize_4x4_game_matrix(self):
        tictactoe = TicTacToe(4)
        test_matrix = np.matrix([[' ', ' ', ' ', ' '],
                                 [' ', ' ', ' ', ' '],
                                 [' ', ' ', ' ', ' '],
                                 [' ', ' ', ' ', ' ']])
        self.assertTrue((test_matrix == tictactoe.game_matrix).all())

    def test_initialize_game_matrix_with_action_sequenz(self):
        action_sequenz = [(0, 0), (3, 2), (0, 3), (1, 0), (1, 3), (2, 0), (3, 0), (0, 2), (3, 1), (2, 2), (2, 1),
                          (1, 1), (0, 1), (1, 2)]
        tictactoe = TicTacToe(4)
        tictactoe.initialize_game_matrix_with_action_sequence(action_sequenz, 'X')
        expected_game_matrix = np.matrix([['X', 'X', 'O', 'X'],
                                          ['O', 'O', 'O', 'X'],
                                          ['O', 'X', 'O', ' '],
                                          ['X', 'X', 'O', ' ']])
        self.assertTrue((expected_game_matrix == tictactoe.game_matrix).all())


class TestPutGameToken(unittest.TestCase):
    def setUp(self):
        self.ticTacToe = TicTacToe(4)
        self.example_ticTacToe_game = TicTacToe(4)
        self.example_ticTacToe_game.put_game_token('X', (0, 0))
        self.example_ticTacToe_game.put_game_token('O', (3, 3))
        self.example_ticTacToe_game.put_game_token('X', (0, 1))
        self.example_ticTacToe_game.put_game_token('O', (2, 2))
        self.example_ticTacToe_game.put_game_token('X', (0, 2))
        self.example_ticTacToe_game.put_game_token('O', (1, 1))
        self.example_ticTacToe_game.put_game_token('X', (0, 3))

    def test_invalid_game_tokens_or_positions(self):
        tictactoe = TicTacToe(4)
        test_matrix = np.matrix([[' ', ' ', ' ', ' '],
                                 [' ', ' ', ' ', ' '],
                                 [' ', ' ', ' ', ' '],
                                 [' ', ' ', ' ', ' ']])
        tictactoe.put_game_token('c', (0, 0))
        tictactoe.put_game_token('Z', (1, 0))
        tictactoe.put_game_token(7, (2, 0))
        tictactoe.put_game_token('X', (4, 4))
        self.assertTrue((tictactoe.game_matrix == test_matrix).all())

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


class TestPossibleMoves(unittest.TestCase):
    def test_16_possible_moves(self):
        tictactoe = TicTacToe(4)
        self.assertEqual(
            [(0, 0), (0, 1), (0, 2), (0, 3), (1, 0), (1, 1), (1, 2), (1, 3), (2, 0), (2, 1), (2, 2), (2, 3), (3, 0),
             (3, 1), (3, 2), (3, 3)], tictactoe.get_possible_moves())

    def test_10_possible_moves(self):
        tictactoe = TicTacToe(4)
        tictactoe.put_game_token('X', (0, 0))
        tictactoe.put_game_token('O', (0, 1))
        tictactoe.put_game_token('X', (0, 2))
        tictactoe.put_game_token('O', (0, 3))
        tictactoe.put_game_token('X', (1, 0))
        tictactoe.put_game_token('O', (2, 0))
        self.assertEqual(
            [(1, 1), (1, 2), (1, 3), (2, 1), (2, 2), (2, 3), (3, 0), (3, 1), (3, 2), (3, 3)],
            tictactoe.get_possible_moves())

    def test_5_possible_moves(self):
        tictactoe = TicTacToe(4)
        tictactoe.put_game_token('X', (0, 0))
        tictactoe.put_game_token('O', (0, 1))
        tictactoe.put_game_token('X', (0, 2))
        tictactoe.put_game_token('O', (0, 3))
        tictactoe.put_game_token('X', (1, 0))
        tictactoe.put_game_token('O', (2, 0))
        tictactoe.put_game_token('X', (3, 0))
        tictactoe.put_game_token('O', (1, 1))
        tictactoe.put_game_token('X', (1, 2))
        tictactoe.put_game_token('O', (2, 1))
        tictactoe.put_game_token('X', (2, 2))
        self.assertEqual([(1, 3), (2, 3), (3, 1), (3, 2), (3, 3)], tictactoe.get_possible_moves())


class TestHorizontalVictory(unittest.TestCase):
    def setUp(self):
        self.example_ticTacToe_game = TicTacToe(4)
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
        self.example_ticTacToe_game = TicTacToe(4)
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
        self.example_ticTacToe_game = TicTacToe(4)
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
        example_tictactoe = TicTacToe(4)
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


class TestVictory(unittest.TestCase):
    def setUp(self):
        self.example_ticTacToe_game = TicTacToe(4)
        self.example_ticTacToe_game.put_game_token('X', (0, 0))
        self.example_ticTacToe_game.put_game_token('O', (0, 1))
        self.example_ticTacToe_game.put_game_token('X', (0, 2))
        self.example_ticTacToe_game.put_game_token('O', (0, 3))
        self.example_ticTacToe_game.put_game_token('X', (1, 0))
        self.example_ticTacToe_game.put_game_token('O', (2, 0))
        self.example_ticTacToe_game.put_game_token('X', (1, 1))
        self.example_ticTacToe_game.put_game_token('O', (2, 1))
        self.example_ticTacToe_game.put_game_token('X', (1, 2))
        self.example_ticTacToe_game.put_game_token('O', (3, 0))
        self.example_ticTacToe_game.put_game_token('X', (2, 2))
        self.example_ticTacToe_game.put_game_token('O', (3, 1))

    def test_no_victory(self):
        self.assertFalse(self.example_ticTacToe_game.is_victory())

    def test_only_horizontal_victory(self):
        self.example_ticTacToe_game.put_game_token('X', (1, 3))
        self.assertTrue(self.example_ticTacToe_game.is_victory())

    def test_only_vertical_victory(self):
        self.example_ticTacToe_game.put_game_token('X', (3, 2))
        self.assertTrue(self.example_ticTacToe_game.is_victory())

    def test_only_diagonal_victory(self):
        self.example_ticTacToe_game.put_game_token('X', (3, 3))
        self.assertTrue(self.example_ticTacToe_game.is_victory())


def suite():
    """Returns an aggregation(called test suite)
    of all test cases in this test module"""
    suite1 = unittest.TestLoader().loadTestsFromTestCase(TestInitializeTicTacToe)
    suite2 = unittest.TestLoader().loadTestsFromTestCase(TestPutGameToken)
    suite3 = unittest.TestLoader().loadTestsFromTestCase(TestPossibleMoves)
    suite4 = unittest.TestLoader().loadTestsFromTestCase(TestHorizontalVictory)
    suite5 = unittest.TestLoader().loadTestsFromTestCase(TestVerticalVictory)
    suite6 = unittest.TestLoader().loadTestsFromTestCase(TestDiagonalVictory)
    suite7 = unittest.TestLoader().loadTestsFromTestCase(TestVictory)
    return unittest.TestSuite([suite1, suite2, suite3, suite4, suite5, suite6, suite7])
