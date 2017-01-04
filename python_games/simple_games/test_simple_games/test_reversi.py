import unittest

from python_games.simple_games.Reversi import Reversi


class TestHorizontalSuggestions(unittest.TestCase):
    def test_two_suggestions(self):
        reversi = Reversi()
        reversi.put_game_token('B', (3, 3))
        reversi.put_game_token('B', (4, 4))
        reversi.put_game_token('W', (3, 4))
        reversi.put_game_token('W', (4, 3))
        self.assertEqual(reversi.suggest_all_moves('B'), [(3, 5), (4, 2)])

    def test_suggestion_with_three_white_token(self):
        reversi = Reversi()
        reversi.put_game_token('B', (3, 3))
        reversi.put_game_token('B', (4, 4))
        reversi.put_game_token('W', (3, 4))
        reversi.put_game_token('W', (4, 3))
        reversi.put_game_token('W', (3, 5))
        reversi.put_game_token('W', (3, 6))
        print(reversi.game_matrix)
        print(reversi.suggest_all_moves('B'))
        self.assertEqual(reversi.suggest_all_moves('B'), [(3, 7), (4, 2)])


def suite():
    """Returns an aggregation(called test suite)
    of all test cases in this test module"""
    suite1 = unittest.TestLoader().loadTestsFromTestCase(TestHorizontalSuggestions)

    return unittest.TestSuite([suite1])
