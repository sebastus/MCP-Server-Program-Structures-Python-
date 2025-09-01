# tools/multiply.py
from .base import BaseTool


class MultiplyTool(BaseTool):
    """Multiply two numbers"""
    
    def _mcp(self, a: int, b: int) -> int:
        """MCP-registered method for multiplying two numbers."""
        return self._core(a, b)
    
    def _core(self, a: int, b: int) -> int:
        """Core implementation: Multiply two numbers.
        
        Args:
            a: First number
            b: Second number
            
        Returns:
            Product of a and b
        """
        return a * b


# Create an instance to register the tool
multiply_tool = MultiplyTool("multiply")
