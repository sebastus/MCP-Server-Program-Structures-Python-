from fastmcp import FastMCP

__all__ = ["subtract", "register_tools"]

def register_tools(mcp: FastMCP) -> None:
    """Register all tools in this module with the MCP server."""
    mcp.tool(subtract)

def subtract(a: int, b: int) -> int:
    """Subtract two numbers"""
    return subtract_core(a, b)

def subtract_core(a: int, b: int) -> int:
    """Core logic for subtracting two numbers"""
    return a - b
