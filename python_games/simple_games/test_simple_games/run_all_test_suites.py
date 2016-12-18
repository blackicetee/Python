import unittest

from python_games.simple_games.test_simple_games import test_validator
from python_games.simple_games.test_simple_games import test_tictactoe

# import test_tictactoe

# Returns the test suite of the test_validator
validator_suite = test_validator.suite()

# Returns the test suite of the test_tictactoe
ticTacToe_suite = test_tictactoe.suite()

# Aggregates all test suites of the system
allTests = unittest.TestSuite([validator_suite, ticTacToe_suite])

# Runs the aggregated tests
unittest.TextTestRunner(verbosity=2).run(allTests)
