# Main + Tools 2

By moving the mcp server to the tools \_\_init\_\_.py, the circular import issue is resolved. And by adding code that iterates over the modules in the tools folder, the issue of keeping the files in the tools package in sync is resolved. An innovation was added - the mcp server tools are registered automatically - but this requires a magic function to be added to each tool.

## Command line for execution

```bash
uv run fastmcp run main.py --transport http --host 127.0.0.1 --port 8000
```

## Command line for tests

```bash
uv run python -m unittest tests.test_add -v
uv run python -m unittest discover -s ./tests -v
```
