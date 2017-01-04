import unittest

from python_games.simple_games.Reversi import Reversi


class TestHorizontalSuggestions(unittest.TestCase):
    def test_two_suggestions(self):
        reversi = Reversi()
        self.assertEqual(reversi.suggest_all_moves('B'), [(3, 5), (4, 2)])


def suite():
    """Returns an aggregation(called test suite)
    of all test cases in this test module"""
    suite1 = unittest.TestLoader().loadTestsFromTestCase(TestHorizontalSuggestions)

    return unittest.TestSuite([suite1])
