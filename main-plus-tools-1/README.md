# Main + Tools 1

This approach is slightly better - it allows for the tools to be better organized in their own package/modules. But it exposes a circular import issue since the tools and main.py both need to import the mcp server object. And - because the tools must be imported in order for them to be registered with the mcp server, the \_\_init\_\_.py must be kept in sync. It's easy to forget this step and waste time.

## Command line for execution

```bash
uv run fastmcp run main.py --transport http --host 127.0.0.1 --port 8000
```
