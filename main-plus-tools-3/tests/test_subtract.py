# tests/test_subtract.py
import unittest
from tools.subtract import SubtractTool


class TestSubtractTool(unittest.TestCase):
    """Test cases for the SubtractTool."""
    
    def setUp(self):
        """Set up test fixtures before each test method."""
        self.subtract_tool = SubtractTool("subtract")
    
    def test_positive_numbers(self):
        """Test subtracting positive numbers."""
        result = self.subtract_tool._core(10, 3)
        self.assertEqual(result, 7)
    
    def test_negative_numbers(self):
        """Test subtracting negative numbers."""
        result = self.subtract_tool._core(-5, -3)
        self.assertEqual(result, -2)
    
    def test_mixed_numbers(self):
        """Test subtracting with mixed signs."""
        result = self.subtract_tool._core(10, -3)
        self.assertEqual(result, 13)
        
        result = self.subtract_tool._core(-10, 3)
        self.assertEqual(result, -13)
    
    def test_zero(self):
        """Test subtracting with zero."""
        result = self.subtract_tool._core(5, 0)
        self.assertEqual(result, 5)
        
        result = self.subtract_tool._core(0, 5)
        self.assertEqual(result, -5)
    
    def test_same_numbers(self):
        """Test subtracting same numbers."""
        result = self.subtract_tool._core(7, 7)
        self.assertEqual(result, 0)


if __name__ == '__main__':
    unittest.main()
