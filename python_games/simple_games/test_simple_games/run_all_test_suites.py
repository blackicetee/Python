import unittest
import test_validator
import test_tictactoe

# Returns the test suite of the test_validator 
validator_suite = test_validator.suite()

# Returns the test suite of the test_tictactoe
tictactoe_suite = test_tictactoe.suite()

# Aggregates all test suites of the system
alltests = unittest.TestSuite([validator_suite, tictactoe_suite])

# Runs the aggregated tests
unittest.TextTestRunner(verbosity=2).run(alltests)
