import os
import importlib
from fastmcp import FastMCP
from .base import BaseTool

# Create the MCP server instance
mcp = FastMCP("Demo 🚀")

# Auto-discover and import all tool modules
def _import_all_tools():
    """Automatically import all tool modules in this package."""
    current_dir = os.path.dirname(__file__)
    
    for filename in os.listdir(current_dir):
        if (filename.endswith('.py') and 
            not filename.startswith('_') and 
            filename != 'base.py'):
            
            module_name = filename[:-3]  # Remove .py extension
            try:
                importlib.import_module(f'.{module_name}', package=__name__)
            except ImportError as e:
                print(f"Warning: Could not import tool module {module_name}: {e}")

# Import the base class and auto-discover all tools
_import_all_tools()

# Export the base class and MCP server for users
__all__ = ["BaseTool", "mcp"]