# tests/test_multiply.py
import unittest
from tools.multiply import MultiplyTool


class TestMultiplyTool(unittest.TestCase):
    """Test cases for the MultiplyTool."""
    
    def setUp(self):
        """Set up test fixtures before each test method."""
        self.multiply_tool = MultiplyTool("multiply")
    
    def test_positive_numbers(self):
        """Test multiplying positive numbers."""
        result = self.multiply_tool._core(5, 3)
        self.assertEqual(result, 15)
    
    def test_negative_numbers(self):
        """Test multiplying negative numbers."""
        result = self.multiply_tool._core(-5, -3)
        self.assertEqual(result, 15)
    
    def test_mixed_numbers(self):
        """Test multiplying with mixed signs."""
        result = self.multiply_tool._core(5, -3)
        self.assertEqual(result, -15)
        
        result = self.multiply_tool._core(-5, 3)
        self.assertEqual(result, -15)
    
    def test_zero(self):
        """Test multiplying with zero."""
        result = self.multiply_tool._core(5, 0)
        self.assertEqual(result, 0)
        
        result = self.multiply_tool._core(0, 5)
        self.assertEqual(result, 0)
    
    def test_one(self):
        """Test multiplying with one."""
        result = self.multiply_tool._core(7, 1)
        self.assertEqual(result, 7)
        
        result = self.multiply_tool._core(1, 7)
        self.assertEqual(result, 7)


if __name__ == '__main__':
    unittest.main()
