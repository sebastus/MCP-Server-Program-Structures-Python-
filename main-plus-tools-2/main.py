from tools import create_mcp_server

# Create the MCP server at module level for fastmcp to find
mcp = create_mcp_server()

if __name__ == "__main__":
    mcp.run()