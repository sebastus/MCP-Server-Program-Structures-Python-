# tools/base.py
from abc import ABC, abstractmethod
from typing import Any, Optional

class BaseTool(ABC):
    """Base class for MCP tools with automatic registration."""

    _instances = {}  # Class variable to store singleton instances

    def __new__(cls, *args, **kwargs):
        """Ensure only one instance per tool class (singleton pattern)."""
        if cls not in cls._instances:
            cls._instances[cls] = super().__new__(cls)
        return cls._instances[cls]

    def __init__(self, name: str, description: Optional[str] = None):
        """Initialize the tool and register it with the MCP server.

        Args:
            name: Tool name (defaults to class name in lowercase)
            description: Tool description (defaults to class docstring)
        """
        
        # Only initialize once (singleton may call __init__ multiple times)
        if hasattr(self, '_initialized'):
            return

        # name the tool
        self.name = name
        self.description = description or f"{self.name} tool"

        # Import mcp here to avoid circular imports and register the tool with mcp server
        from . import mcp
        mcp.tool(name=self.name)(self._mcp)

        self._initialized = True


    @abstractmethod
    def _mcp(self, *args, **kwargs) -> Any:
        """MCP-registered method that calls _core.

        This method should have the exact signature of the tool
        and delegate to _core. Override this in subclasses.
        """
        pass

    @abstractmethod
    def _core(self, *args, **kwargs) -> Any:
        """Core implementation of the tool logic.

        This method contains the actual tool functionality and should be
        implemented by subclasses. It's designed to be easily testable.
        Tests should call this method directly.
        """
        pass
