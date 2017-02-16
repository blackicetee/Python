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
        tictactoe.initialize_game_matrix_with_action_sequence(action_sequenz)
        expected_game_matrix = np.matrix([['X', 'X', 'O', 'X'],
                                          ['O', 'O', 'O', 'X'],
                                          ['O', 'X', 'O', ' '],
                                          ['X', 'X', 'O', ' ']])
        self.assertTrue((expected_game_matrix == tictactoe.game_matrix).all())


class TestPrintableGameMatrix(unittest.TestCase):
    def test_four_times_four_printable_game_matrix(self):
        action_sequenz = [(0, 0), (3, 2), (0, 3), (1, 0), (1, 3), (2, 0), (3, 0), (0, 2), (3, 1), (2, 2), (2, 1),
                          (1, 1), (0, 1), (1, 2)]
        tictactoe = TicTacToe(4)
        tictactoe.initialize_game_matrix_with_action_sequence(action_sequenz)
        test_game_matrix_string = 'X | X | O | X\n-------------\nO | O | O | X\n-------------\nO | X | O |  \n-------------\nX | X | O |  \n'
        self.assertEqual(tictactoe.printable_game_matrix(), test_game_matrix_string)

    def test_three_times_three_printable_game_matrix(self):
        action_sequenz = [(0, 0), (1, 0), (2, 0), (0, 2), (2, 2), (2, 1), (1, 1), (0, 1), (1, 2)]
        tictactoe = TicTacToe(3)
        tictactoe.initialize_game_matrix_with_action_sequence(action_sequenz)
        test_game_matrix_string = 'X | O | O\n---------\nO | X | X\n---------\nX | O | X\n'
        self.assertEqual(tictactoe.printable_game_matrix(), test_game_matrix_string)


class TestConnectionAnalysis(unittest.TestCase):
    def setUp(self):
        self.tictactoe = TicTacToe(4)
        action_sequenz = [(0, 0), (3, 2), (0, 3), (1, 0), (1, 3), (2, 0), (3, 0), (0, 2), (3, 1), (2, 2), (2, 1),
                          (1, 1), (0, 1), (1, 2)]
        self.tictactoe.initialize_game_matrix_with_action_sequence(action_sequenz)

    def test_get_valid_positions_by_two_positions_1(self):
        self.assertEqual([(0, 0), (1, 1), (2, 2), (3, 3)],
                         self.tictactoe.get_victory_relevant_positions_by_two_given_positions((0, 0), (1, 1)))

    def test_get_valid_positions_by_two_positions_2(self):
        self.assertEqual([(3, 0), (2, 1), (1, 2), (0, 3)],
                         self.tictactoe.get_victory_relevant_positions_by_two_given_positions((3, 0), (1, 2)))

    def test_get_valid_positions_by_two_positions_3(self):
        self.assertEqual([(1, 0), (1, 1), (1, 2), (1, 3)],
                         self.tictactoe.get_victory_relevant_positions_by_two_given_positions((1, 0), (1, 2)))

    def test_get_valid_positions_by_two_positions_4(self):
        self.assertEqual([(0, 1), (1, 1), (2, 1), (3, 1)],
                         self.tictactoe.get_victory_relevant_positions_by_two_given_positions((2, 1), (0, 1)))

    def test_is_connection_pure_1(self):
        self.assertTrue(self.tictactoe.is_connection_pure((0, 3), (1, 3), 'X'))

    def test_is_connection_pure_2(self):
        self.assertTrue(self.tictactoe.is_connection_pure((0, 3), (3, 3), 'X'))

    def test_is_connection_pure_3(self):
        self.assertFalse(self.tictactoe.is_connection_pure((1, 1), (1, 2), 'O'))

    def test_is_connection_pure_4(self):
        self.assertFalse(self.tictactoe.is_connection_pure((1, 1), (1, 2), 'X'))

    def test_is_connection_pure_5(self):
        self.assertTrue(self.tictactoe.is_connection_pure((1, 2), (3, 2), 'O'))

    def test_is_connection_pure_6(self):
        self.assertFalse(self.tictactoe.is_connection_pure((1, 1), (2, 2), 'O'))

    def test_is_connection_pure_7(self):
        tictactoe = TicTacToe(4)
        action_sequence = [(0, 0), (3, 0), (1, 1), (2, 1), (2, 2), (1, 2), (3, 3)]
        tictactoe.initialize_game_matrix_with_action_sequence(action_sequence)
        self.assertTrue(tictactoe.is_connection_pure((1, 1), (2, 2), 'X'))

    def test_is_connection_pure_8(self):
        tictactoe = TicTacToe(4)
        action_sequence = [(0, 0), (3, 0), (1, 1), (2, 1), (2, 2), (1, 2), (3, 2), (0, 3)]
        tictactoe.initialize_game_matrix_with_action_sequence(action_sequence)
        self.assertTrue(tictactoe.is_connection_pure((3, 0), (1, 2), 'O'))

    def test_count_tokens_in_pure_connection_1(self):
        tictactoe = TicTacToe(4)
        action_sequence = [(0, 0), (3, 0), (1, 1), (2, 1), (2, 2), (1, 2), (3, 2), (0, 3)]
        tictactoe.initialize_game_matrix_with_action_sequence(action_sequence)
        self.assertEqual(3, tictactoe.count_tokens_in_pure_connection((0, 0), (1, 1), 'X'))

    def test_count_tokens_in_pure_connection_2(self):
        tictactoe = TicTacToe(4)
        action_sequence = [(0, 0), (3, 0), (1, 1), (2, 1), (2, 2), (1, 2), (3, 2), (0, 3)]
        tictactoe.initialize_game_matrix_with_action_sequence(action_sequence)
        self.assertEqual(4, tictactoe.count_tokens_in_pure_connection((3, 0), (1, 2), 'O'))

    def test_count_tokens_in_pure_connection_3(self):
        tictactoe = TicTacToe(4)
        action_sequence = [(0, 0), (3, 0), (1, 1), (2, 1), (2, 2), (1, 2), (3, 2), (0, 3)]
        tictactoe.initialize_game_matrix_with_action_sequence(action_sequence)
        self.assertEqual(0, tictactoe.count_tokens_in_pure_connection((0, 0), (3, 0), 'O'))

    def test_count_tokens_in_pure_connection_4(self):
        tictactoe = TicTacToe(4)
        action_sequence = [(0, 0), (3, 0), (1, 1), (2, 1), (2, 2), (1, 2), (3, 2), (0, 3)]
        tictactoe.initialize_game_matrix_with_action_sequence(action_sequence)
        self.assertEqual(0, tictactoe.count_tokens_in_pure_connection((2, 2), (3, 2), 'X'))


class TestUndoMove(unittest.TestCase):
    def test_undo_move_1(self):
        tictactoe = TicTacToe(4)
        action_sequence = [(0, 0), (3, 0), (1, 1), (2, 1), (2, 2), (1, 2), (3, 2), (0, 3)]
        tictactoe.initialize_game_matrix_with_action_sequence(action_sequence)
        tictactoe.undo_move()
        expected_game_matrix = np.matrix(
            [['X', ' ', ' ', ' '], [' ', 'X', 'O', ' '], [' ', 'O', 'X', ' '], ['O', ' ', 'X', ' ']])
        self.assertTrue((expected_game_matrix == tictactoe.game_matrix).all())

    def test_undo_move_2(self):
        tictactoe = TicTacToe(4)
        action_sequence = [(0, 0), (3, 0), (1, 1), (2, 1), (2, 2), (1, 2), (3, 2), (0, 3)]
        tictactoe.initialize_game_matrix_with_action_sequence(action_sequence)
        tictactoe.undo_move()
        tictactoe.undo_move()
        tictactoe.undo_move()
        tictactoe.undo_move()
        tictactoe.undo_move()
        expected_game_matrix = np.matrix(
            [['X', ' ', ' ', ' '], [' ', 'X', ' ', ' '], [' ', ' ', ' ', ' '], ['O', ' ', ' ', ' ']])
        self.assertTrue((expected_game_matrix == tictactoe.game_matrix).all())

    def test_undo_move_3(self):
        tictactoe = TicTacToe(4)
        tictactoe.make_move((0, 0))
        tictactoe.make_move((1, 0))
        tictactoe.make_move((0, 1))
        tictactoe.make_move((2, 0))
        tictactoe.make_move((0, 3))
        tictactoe.undo_move()
        tictactoe.undo_move()
        action_sequence = [(0, 0), (1, 0), (0, 1)]
        expected_tictactoe_game = TicTacToe(4)
        expected_tictactoe_game.initialize_game_matrix_with_action_sequence(action_sequence)
        self.assertTrue((expected_tictactoe_game.game_matrix == tictactoe.game_matrix).all())


class TestMakeMove(unittest.TestCase):
    def setUp(self):
        self.ticTacToe = TicTacToe(4)
        self.example_ticTacToe_game = TicTacToe(4)
        self.example_ticTacToe_game.make_move((0, 0))
        self.example_ticTacToe_game.make_move((3, 3))
        self.example_ticTacToe_game.make_move((0, 1))
        self.example_ticTacToe_game.make_move((2, 2))
        self.example_ticTacToe_game.make_move((0, 2))
        self.example_ticTacToe_game.make_move((1, 1))
        self.example_ticTacToe_game.make_move((0, 3))

    def test_put_seven_game_tokens(self):
        self.ticTacToe.make_move((0, 0))
        self.ticTacToe.make_move((3, 3))
        self.ticTacToe.make_move((0, 1))
        self.ticTacToe.make_move((2, 2))
        self.ticTacToe.make_move((0, 2))
        self.ticTacToe.make_move((1, 1))
        self.ticTacToe.make_move((0, 3))
        equality_matrix = self.example_ticTacToe_game.game_matrix == self.ticTacToe.game_matrix
        self.assertTrue(equality_matrix.all())

    def test_if_value_not_changes_when_position_is_taken(self):
        copy_example_ticTacToe_game = self.example_ticTacToe_game
        copy_example_ticTacToe_game.make_move((0, 0))
        copy_example_ticTacToe_game.make_move((3, 3))
        copy_example_ticTacToe_game.make_move((0, 1))
        copy_example_ticTacToe_game.make_move((2, 2))
        self.assertTrue((copy_example_ticTacToe_game.game_matrix == self.example_ticTacToe_game.game_matrix).all())


class TestPossibleMoves(unittest.TestCase):
    def test_16_possible_moves(self):
        tictactoe = TicTacToe(4)
        self.assertEqual(
            [(0, 0), (0, 1), (0, 2), (0, 3), (1, 0), (1, 1), (1, 2), (1, 3), (2, 0), (2, 1), (2, 2), (2, 3), (3, 0),
             (3, 1), (3, 2), (3, 3)], tictactoe.get_possible_moves())

    def test_10_possible_moves(self):
        tictactoe = TicTacToe(4)
        tictactoe.make_move((0, 0))
        tictactoe.make_move((0, 1))
        tictactoe.make_move((0, 2))
        tictactoe.make_move((0, 3))
        tictactoe.make_move((1, 0))
        tictactoe.make_move((2, 0))
        self.assertEqual(
            [(1, 1), (1, 2), (1, 3), (2, 1), (2, 2), (2, 3), (3, 0), (3, 1), (3, 2), (3, 3)],
            tictactoe.get_possible_moves())

    def test_5_possible_moves(self):
        tictactoe = TicTacToe(4)
        tictactoe.make_move((0, 0))
        tictactoe.make_move((0, 1))
        tictactoe.make_move((0, 2))
        tictactoe.make_move((0, 3))
        tictactoe.make_move((1, 0))
        tictactoe.make_move((2, 0))
        tictactoe.make_move((3, 0))
        tictactoe.make_move((1, 1))
        tictactoe.make_move((1, 2))
        tictactoe.make_move((2, 1))
        tictactoe.make_move((2, 2))
        self.assertEqual([(1, 3), (2, 3), (3, 1), (3, 2), (3, 3)], tictactoe.get_possible_moves())


class TestHorizontalVictory(unittest.TestCase):
    def setUp(self):
        self.example_ticTacToe_game = TicTacToe(4)
        self.example_ticTacToe_game.make_move((2, 0))
        self.example_ticTacToe_game.make_move((3, 3))
        self.example_ticTacToe_game.make_move((2, 1))
        self.example_ticTacToe_game.make_move((1, 1))
        self.example_ticTacToe_game.make_move((2, 2))
        self.example_ticTacToe_game.make_move((0, 0))

    def test_horizontal_victory(self):
        self.example_ticTacToe_game.make_move((2, 3))
        self.assertTrue(self.example_ticTacToe_game.is_horizontal_victory())

    def test_no_horizontal_victory(self):
        self.assertFalse(self.example_ticTacToe_game.is_horizontal_victory())


class TestVerticalVictory(unittest.TestCase):
    def setUp(self):
        self.example_ticTacToe_game = TicTacToe(4)
        self.example_ticTacToe_game.make_move((0, 0))
        self.example_ticTacToe_game.make_move((3, 3))
        self.example_ticTacToe_game.make_move((1, 0))
        self.example_ticTacToe_game.make_move((2, 3))
        self.example_ticTacToe_game.make_move((2, 0))
        self.example_ticTacToe_game.make_move((1, 3))

    def test_vertical_victory(self):
        self.example_ticTacToe_game.make_move((3, 0))
        self.assertTrue(self.example_ticTacToe_game.is_vertical_victory())

    def test_no_vertical_victory(self):
        self.assertFalse(self.example_ticTacToe_game.is_vertical_victory())


class TestDiagonalVictory(unittest.TestCase):
    def setUp(self):
        self.example_ticTacToe_game = TicTacToe(4)
        self.example_ticTacToe_game.make_move((0, 0))
        self.example_ticTacToe_game.make_move((3, 0))
        self.example_ticTacToe_game.make_move((1, 1))
        self.example_ticTacToe_game.make_move((3, 1))
        self.example_ticTacToe_game.make_move((2, 2))
        self.example_ticTacToe_game.make_move((3, 2))

    def test_diagonal_victory_top_left_to_bottom_right(self):
        self.example_ticTacToe_game.make_move((3, 3))
        self.assertTrue(self.example_ticTacToe_game.is_diagonal_victory())

    def test_digital_victory_top_right_to_bottom_left(self):
        example_tictactoe = TicTacToe(4)
        example_tictactoe.make_move((0, 3))
        example_tictactoe.make_move((0, 0))
        example_tictactoe.make_move((1, 2))
        example_tictactoe.make_move((1, 0))
        example_tictactoe.make_move((2, 1))
        example_tictactoe.make_move((2, 0))
        example_tictactoe.make_move((3, 0))
        self.assertTrue(example_tictactoe.is_diagonal_victory())

    def test_no_digital_victory(self):
        self.assertFalse(self.example_ticTacToe_game.is_vertical_victory())


class TestVictory(unittest.TestCase):
    def setUp(self):
        self.example_ticTacToe_game = TicTacToe(4)
        self.example_ticTacToe_game.make_move((0, 0))
        self.example_ticTacToe_game.make_move((0, 1))
        self.example_ticTacToe_game.make_move((0, 2))
        self.example_ticTacToe_game.make_move((0, 3))
        self.example_ticTacToe_game.make_move((1, 0))
        self.example_ticTacToe_game.make_move((2, 0))
        self.example_ticTacToe_game.make_move((1, 1))
        self.example_ticTacToe_game.make_move((2, 1))
        self.example_ticTacToe_game.make_move((1, 2))
        self.example_ticTacToe_game.make_move((3, 0))
        self.example_ticTacToe_game.make_move((2, 2))
        self.example_ticTacToe_game.make_move((3, 1))

    def test_no_victory(self):
        self.assertFalse(self.example_ticTacToe_game.is_victory())

    def test_only_horizontal_victory(self):
        self.example_ticTacToe_game.make_move((1, 3))
        self.assertTrue(self.example_ticTacToe_game.is_victory())

    def test_only_vertical_victory(self):
        self.example_ticTacToe_game.make_move((3, 2))
        self.assertTrue(self.example_ticTacToe_game.is_victory())

    def test_only_diagonal_victory(self):
        self.example_ticTacToe_game.make_move((3, 3))
        self.assertTrue(self.example_ticTacToe_game.is_victory())


def suite():
    """Returns an aggregation(called test suite)
    of all test cases in this test module"""
    suite1 = unittest.TestLoader().loadTestsFromTestCase(TestInitializeTicTacToe)
    suite2 = unittest.TestLoader().loadTestsFromTestCase(TestPrintableGameMatrix)
    suite3 = unittest.TestLoader().loadTestsFromTestCase(TestMakeMove)
    suite4 = unittest.TestLoader().loadTestsFromTestCase(TestPossibleMoves)
    suite5 = unittest.TestLoader().loadTestsFromTestCase(TestHorizontalVictory)
    suite6 = unittest.TestLoader().loadTestsFromTestCase(TestVerticalVictory)
    suite7 = unittest.TestLoader().loadTestsFromTestCase(TestDiagonalVictory)
    suite8 = unittest.TestLoader().loadTestsFromTestCase(TestVictory)
    return unittest.TestSuite([suite1, suite2, suite3, suite4, suite5, suite6, suite7, suite8])
