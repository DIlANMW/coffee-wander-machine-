import unittest
from unittest.mock import patch

from machine import menu, buy_coffee


class TestListSum(unittest.TestCase):

    string_of_ints = '1'
    string_of_ints1 = '1'

    @patch('builtins.input', return_value=string_of_ints)
    def test_sum_string_of_ints(self, mock_input):
        result = menu()
        self.assertEqual(result,buy_coffee() )

    @patch('builtins.input', return_value=string_of_ints)
    def test_sum_string_of_ints1(self, mock_input):
        result = menu()
        self.assertNotEqual(result, buy_coffee())

if __name__ == '__main__':
    unittest.main()