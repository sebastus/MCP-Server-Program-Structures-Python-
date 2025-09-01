# main.py 

from server import mcp
import tools  # F401 import tools to ensure they are registered

if __name__ == "__main__":
    mcp.run()