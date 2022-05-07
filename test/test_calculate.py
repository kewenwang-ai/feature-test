# pylint:disable=relative-beyond-top-level
"""Unittest of calculator
"""

import unittest

from .calculate import Calculator


class TestCalculate(unittest.TestCase):
    """Test
    """

    def test_add(self):
        """Test add
        """
        cal = Calculator()
        num_1, num_2 = 10, 20
        result = cal.add(num_1, num_2)
        self.assertEqual(result, num_1 + num_2)

    def test_multiply(self):
        """Test Multiply
        """
        cal = Calculator()
        num_1, num_2 = 10, 20
        result = cal.multiply(num_1, num_2)
        self.assertEqual(result, num_1 * num_2)
