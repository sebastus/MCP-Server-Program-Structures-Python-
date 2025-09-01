# main.py 

import tools  # Import tools to ensure they are registered and get access to mcp

# Expose the mcp server for FastMCP CLI
mcp = tools.mcp

if __name__ == "__main__":
    mcp.run()