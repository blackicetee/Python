"""This self written python module will handle different kinds of user input and validate it"""

# This is a module for regular expressions see python documentation "Regular expression operations"
import re


class MyValidator:
    @staticmethod
    def is_valid_from_zero_to_three(user_input):
        regex_pattern = r'[0-3]'
        if re.match(regex_pattern, user_input) is not None:
            return True
        else:
            return False
