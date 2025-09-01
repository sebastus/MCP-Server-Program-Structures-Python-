from fastmcp import FastMCP

__all__ = ["add", "register_tools"]

def register_tools(mcp: FastMCP) -> None:
    """Register all tools in this module with the MCP server."""
    mcp.tool(add)

def add(a: int, b: int) -> int:
    """Add two numbers"""
    return a + b

