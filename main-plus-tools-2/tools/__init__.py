import importlib
import pkgutil
from fastmcp import FastMCP

def create_mcp_server(name: str = "Demo 🚀") -> FastMCP:
    """Create and configure an MCP server with all tools."""
    mcp = FastMCP(name)
    
    # Auto-discover and register all tools
    _register_all_tools(mcp)
    
    return mcp

def _register_all_tools(mcp: FastMCP) -> None:
    """Automatically discover and register all tools in the tools package."""
    import tools
    
    # Get all modules in the tools package
    for importer, modname, ispkg in pkgutil.iter_modules(tools.__path__, tools.__name__ + "."):
        if modname == __name__:  # Skip this __init__ module
            continue
            
        try:
            # Import the module
            module = importlib.import_module(modname)
            
            # If it has a register_tools function, call it
            if hasattr(module, 'register_tools'):
                module.register_tools(mcp)
                print(f"Registered tools from {modname}")
        except Exception as e:
            print(f"Warning: Could not register tools from {modname}: {e}")

__all__ = ["create_mcp_server"]
