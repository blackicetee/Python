import unittest

from python_games.simple_games.Reversi import Reversi


class TestSuggestionsForBlackTokens(unittest.TestCase):
    def test_two_suggestions(self):
        reversi = Reversi()
        reversi.put_game_token('B', (3, 3))
        reversi.put_game_token('B', (4, 4))
        reversi.put_game_token('W', (3, 4))
        reversi.put_game_token('W', (4, 3))
        self.assertEqual(reversi.suggest_all_moves('B'), [(3, 5), (5, 3), (4, 2), (2, 4)])

    def test_suggestion_with_three_white_token(self):
        reversi = Reversi()
        reversi.put_game_token('B', (3, 3))
        reversi.put_game_token('B', (4, 4))
        reversi.put_game_token('W', (3, 4))
        reversi.put_game_token('W', (4, 3))
        reversi.put_game_token('W', (3, 5))
        reversi.put_game_token('W', (3, 6))
        self.assertEqual(reversi.suggest_all_moves('B'), [(3, 7), (5, 3), (4, 2), (2, 4), (2, 6)])

    def test_multiple_suggestions(self):
        reversi = Reversi()
        reversi.put_game_token('B', (3, 3))
        reversi.put_game_token('B', (4, 4))
        reversi.put_game_token('B', (3, 2))
        reversi.put_game_token('B', (3, 1))
        reversi.put_game_token('W', (3, 4))
        reversi.put_game_token('W', (4, 3))
        reversi.put_game_token('W', (3, 5))
        reversi.put_game_token('W', (3, 6))
        reversi.put_game_token('W', (2, 2))
        reversi.put_game_token('W', (1, 2))
        reversi.put_game_token('W', (3, 0))
        reversi.put_game_token('W', (4, 1))
        self.assertEqual(reversi.suggest_all_moves('B'),
                         [(5, 1), (1, 3), (0, 2), (5, 4), (5, 0), (3, 7), (5, 3), (1, 1), (4, 2), (2, 4), (2, 6)])


class TestSuggestionsForWhiteTokens(unittest.TestCase):
    def test_multiple_suggestions(self):
        reversi = Reversi()
        reversi.put_game_token('B', (3, 3))
        reversi.put_game_token('B', (4, 4))
        reversi.put_game_token('B', (3, 2))
        reversi.put_game_token('B', (3, 1))
        reversi.put_game_token('W', (3, 4))
        reversi.put_game_token('W', (4, 3))
        reversi.put_game_token('W', (3, 5))
        reversi.put_game_token('W', (3, 6))
        reversi.put_game_token('W', (2, 2))
        reversi.put_game_token('W', (1, 2))
        reversi.put_game_token('W', (3, 0))
        reversi.put_game_token('W', (4, 1))
        self.assertEqual(reversi.suggest_all_moves('W'),
                         [(4, 2), (5, 5), (4, 0), (5, 4), (5, 3), (2, 1), (2, 3), (4, 5), (2, 3), (2, 1)])


def suite():
    """Returns an aggregation(called test suite)
    of all test cases in this test module"""
    suite1 = unittest.TestLoader().loadTestsFromTestCase(TestSuggestionsForBlackTokens)
    suite2 = unittest.TestLoader().loadTestsFromTestCase(TestSuggestionsForWhiteTokens)

    return unittest.TestSuite([suite1, suite2])
