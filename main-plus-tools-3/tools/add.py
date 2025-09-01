from .base import BaseTool


class AddTool(BaseTool):
    """Add two numbers"""
    
    def _mcp(self, a: int, b: int) -> int:
        """MCP-registered method for adding two numbers."""
        return self._core(a, b)
    
    def _core(self, a: int, b: int) -> int:
        """Core implementation: Add two numbers.
        
        Args:
            a: First number
            b: Second number
            
        Returns:
            Sum of a and b
        """
        return a + b


# Create an instance to register the tool
add_tool = AddTool("add")

