import unittest
import sys
import os

# Add the parent directory to the path so we can import from tools
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from tools.add import add


class TestAddFunction(unittest.TestCase):
    """Test cases for the add function."""

    def test_add_positive_numbers(self):
        """Test adding two positive numbers."""
        result = add(5, 3)
        self.assertEqual(result, 8)

    def test_add_negative_numbers(self):
        """Test adding two negative numbers."""
        result = add(-5, -3)
        self.assertEqual(result, -8)

    def test_add_positive_and_negative(self):
        """Test adding a positive and negative number."""
        result = add(10, -3)
        self.assertEqual(result, 7)

    def test_add_with_zero(self):
        """Test adding with zero."""
        result = add(5, 0)
        self.assertEqual(result, 5)
        
        result = add(0, 5)
        self.assertEqual(result, 5)

    def test_add_zero_with_zero(self):
        """Test adding zero with zero."""
        result = add(0, 0)
        self.assertEqual(result, 0)

    def test_add_large_numbers(self):
        """Test adding large numbers."""
        result = add(1000000, 2000000)
        self.assertEqual(result, 3000000)

    def test_add_returns_int(self):
        """Test that the function returns an integer."""
        result = add(1, 2)
        self.assertIsInstance(result, int)

    def test_add_commutative_property(self):
        """Test that addition is commutative (a + b = b + a)."""
        a, b = 7, 13
        result1 = add(a, b)
        result2 = add(b, a)
        self.assertEqual(result1, result2)


if __name__ == '__main__':
    unittest.main()