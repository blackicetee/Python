import unittest

# Imports the self written python module validator
import validator

class TestIsValidFromZeroToThree(unittest.TestCase):
    """Tests if user input is 0, 1, 2 or 3"""
    def test_input_zero(self):
        self.assertTrue(validator.is_valid_from_zero_to_three('0'))

    def test_input_one(self):
        self.assertTrue(validator.is_valid_from_zero_to_three('1'))
   
    def test_input_two(self):
        self.assertTrue(validator.is_valid_from_zero_to_three('2'))

    def test_input_three(self):
        self.assertTrue(validator.is_valid_from_zero_to_three('3'))
 
def suite():
    """Returns an aggregation(called test suite) 
    of all test cases in this test module"""
    suite1 = unittest.TestLoader().loadTestsFromTestCase(TestIsValidFromZeroToThree)
    allsuites = unittest.TestSuite([suite1])
    return allsuites
