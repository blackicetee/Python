import unittest

from python_games.simple_games.Reversi import Reversi


class TestSuggestionsForBlackTokens(unittest.TestCase):
    def test_two_suggestions(self):
        reversi = Reversi()
        reversi.put_game_token('B', (3, 3))
        reversi.put_game_token('B', (4, 4))
        reversi.put_game_token('W', (3, 4))
        reversi.put_game_token('W', (4, 3))
        self.assertEqual(reversi.suggest_all_moves('B'), [(2, 4), (3, 5), (4, 2), (5, 3)])

    def test_suggestion_with_three_white_token(self):
        reversi = Reversi()
        reversi.put_game_token('B', (3, 3))
        reversi.put_game_token('B', (4, 4))
        reversi.put_game_token('W', (3, 4))
        reversi.put_game_token('W', (4, 3))
        reversi.put_game_token('W', (3, 5))
        reversi.put_game_token('W', (3, 6))
        self.assertEqual(reversi.suggest_all_moves('B'), [(2, 4), (2, 6), (3, 7), (4, 2), (5, 3) ])

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
                         [(0, 2), (1, 1), (1, 3), (2, 4), (2, 6), (3, 7), (4, 2), (5, 0), (5, 1), (5, 3), (5, 4)])



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
                         [(2, 1), (2, 3), (4, 0), (4, 2),  (4, 5), (5, 3), (5, 4), (5, 5)])

class TestCountTokens(unittest.TestCase):
    def test_count_eight_black_tokens(self):
        reversi = Reversi()
        reversi.put_game_token('B', (3, 3))
        reversi.put_game_token('B', (4, 4))
        reversi.put_game_token('B', (3, 2))
        reversi.put_game_token('B', (3, 1))
        reversi.put_game_token('B', (3, 4))
        reversi.put_game_token('B', (4, 3))
        reversi.put_game_token('B', (3, 5))
        reversi.put_game_token('B', (3, 6))
        self.assertEqual(reversi.count_black_game_tokens(), 8)

    def test_count_four_black_tokens(self):
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
        self.assertEqual(reversi.count_black_game_tokens(), 4)

    def test_count_zero_white_tokens(self):
        reversi = Reversi()
        reversi.put_game_token('B', (3, 3))
        reversi.put_game_token('B', (4, 4))
        reversi.put_game_token('B', (3, 2))
        reversi.put_game_token('B', (3, 1))
        reversi.put_game_token('B', (3, 4))
        reversi.put_game_token('B', (4, 3))
        reversi.put_game_token('B', (3, 5))
        reversi.put_game_token('B', (3, 6))
        self.assertEqual(reversi.count_white_game_tokens(), 0)

    def test_count_eight_white_tokens(self):
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
        self.assertEqual(reversi.count_white_game_tokens(), 8)


def suite():
    """Returns an aggregation(called test suite)
    of all test cases in this test module"""
    suite1 = unittest.TestLoader().loadTestsFromTestCase(TestSuggestionsForBlackTokens)
    suite2 = unittest.TestLoader().loadTestsFromTestCase(TestSuggestionsForWhiteTokens)
    suite3 = unittest.TestLoader().loadTestsFromTestCase(TestCountTokens)

    return unittest.TestSuite([suite1, suite2, suite3])
