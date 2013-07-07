#!/usr/bin/env python

import unittest
import sys
import myapp

class MyAppTests(unittest.TestCase):
    """Unit testing"""

    def setUp(self):
        self.a_val = 10
        self.b_val = 5

    def test_sum1(self):
        self.assertEqual(myapp.sum(self.a_val, self.b_val), 15)

    def test_diff1(self):
        self.assertEqual(myapp.difference(self.a_val, self.b_val), 5)

if __name__ == '__main__':
    unittest.main()

