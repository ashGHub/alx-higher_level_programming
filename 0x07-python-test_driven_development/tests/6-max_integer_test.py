#!/usr/bin/python3
"""
Module to to unit test max_integer function
"""

import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxIntger(unittest.TestCase):
    """
    Test cases class for max integer function
    """

    def test_empty_list(self):
        self.assertEqual(max_integer(), None)

    def test_one_element(self):
        self.assertEqual(max_integer([6]), 6)

    def test_two_equal_element(self):
        self.assertEqual(max_integer([4, 4]), 4)

    def test_three_element_two_equal_one_min(self):
        self.assertEqual(max_integer([7, 7, 5]), 7)

    def test_max_at_the_beginning(self):
        self.assertEqual(max_integer([10, 3, 4, 6, 2, 1]), 10)

    def test_max_in_the_middle(self):
        self.assertEqual(max_integer([9, 8, 7, 6]), 9)

    def test_one_negative_number_in_the_list(self):
        self.assertEqual(max_integer([-10, 9, 8, 0, 5]), 9)

    def test_all_negative_numbers_in_the_list(self):
        self.assertEqual(max_integer([-1, -2, -19, -8]), -1)

    def test_max_at_the_end(self):
        self.assertEqual(max_integer([9, 10, 5, 3, 11, 34, 59]), 59)


if __name__ == '__main__':
    unittest.main()
