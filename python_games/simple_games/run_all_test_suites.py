import unittest
import test_validator

# Returns the test suite of the test_validator 
validator_suite = test_validator.suite()

# Aggregates all test suites of the system
alltests = unittest.TestSuite([validator_suite])

# Runs the aggregated tests
unittest.TextTestRunner(verbosity=2).run(alltests)
