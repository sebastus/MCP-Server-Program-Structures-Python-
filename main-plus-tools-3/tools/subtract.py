from .base import BaseTool


class SubtractTool(BaseTool):
    """Subtract two numbers"""
    
    def _mcp(self, a: int, b: int) -> int:
        """MCP-registered method for subtracting two numbers."""
        return self._core(a, b)
    
    def _core(self, a: int, b: int) -> int:
        """Core implementation: Subtract two numbers.
        
        Args:
            a: First number
            b: Second number
            
        Returns:
            Difference of a and b (a - b)
        """
        return a - b


# Create an instance to register the tool
subtract_tool = SubtractTool("subtract")

