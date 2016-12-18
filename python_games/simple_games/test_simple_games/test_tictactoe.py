import unittest
from numpy import shape

# Will import the absolute system path to directory simple_games 
# where the TicTacToe module is located
import sys
sys.path.insert(0, '/home/thilo/Python/python_games/simple_games')

from tictactoe import TicTacToe

class TestInitializeTicTacToe(unittest.TestCase):
	"""Tests if the matrix shape of an initialized
	TicTacToe game is correct."""

	def test_initialize_4x4_tictactoe_matrix(self):
		ttt_4x4 = TicTacToe(4, 4) 
		self.assertEqual((4,4), shape(ttt_4x4.game_matrix))

	def test_initialize_8x8_tictactoe_matrix(self):
		ttt_8x8 = TicTacToe(8, 8)
		self.assertEqual((8, 8), shape(ttt_8x8.game_matrix))

class TestTranslateGameTokenType(unittest.TestCase):
	"""Tests if game token type is translated correctly into predefined
	float values or otherwise a value error exception is raced."""

	def setUp(self):
		self.tictactoe = TicTacToe(4, 4)

	def test_translate_game_token_O(self):
		self.assertEqual(1.0, self.tictactoe.translate_game_token_type('O'))

	def test_translate_game_token_X(self):
		self.assertEqual(2.0, self.tictactoe.translate_game_token_type('X'))

def suite():
	"""Returns an aggregation(called test suite) 
	of all test cases in this test module"""
	suite1 = unittest.TestLoader().loadTestsFromTestCase(TestInitializeTicTacToe)
	suite2 = unittest.TestLoader().loadTestsFromTestCase(TestTranslateGameTokenType)
	allsuites = unittest.TestSuite([suite1, suite2])
	return allsuites
