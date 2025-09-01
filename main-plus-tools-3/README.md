# Main + Tools 3 (Object oriented)

This version adds a base class for the tools. The base class:

1. Enforces singleton per tool type
2. Registers the tool with the MCP server
3. Ensures each tool is registered only once

The base class has two abstract methods:

1. _mcp - the mcp wrapper function
2. _core - the core functionality

## Testing

There are several examples of tests. They have a simple structure:

1. Create an instance of the tool to be tested
2. Call the tool's _core function
3. Assert

## Command line for execution

```bash
uv run fastmcp run main.py --transport http --host 127.0.0.1 --port 8000
```

## Command line for tests

```bash
uv run python -m unittest discover -s ./tests
```
