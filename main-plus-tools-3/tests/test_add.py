# tests/test_add.py
import unittest
from tools.add import AddTool


class TestAddTool(unittest.TestCase):
    """Test cases for the AddTool."""
    
    def setUp(self):
        """Set up test fixtures before each test method."""
        self.add_tool = AddTool()
    
    def test_positive_numbers(self):
        """Test adding positive numbers."""
        result = self.add_tool._core(5, 3)
        self.assertEqual(result, 8)
    
    def test_negative_numbers(self):
        """Test adding negative numbers."""
        result = self.add_tool._core(-5, -3)
        self.assertEqual(result, -8)
    
    def test_mixed_numbers(self):
        """Test adding positive and negative numbers."""
        result = self.add_tool._core(10, -3)
        self.assertEqual(result, 7)
    
    def test_zero(self):
        """Test adding with zero."""
        result = self.add_tool._core(5, 0)
        self.assertEqual(result, 5)
        
        result = self.add_tool._core(0, 0)
        self.assertEqual(result, 0)


if __name__ == '__main__':
    unittest.main()
