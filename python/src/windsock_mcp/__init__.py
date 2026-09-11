"""Windsock aircraft intelligence for AI agents.

* :func:`connect` — async context manager yielding an initialized
  :class:`mcp.ClientSession` to the remote Windsock MCP server
  (``https://windsock.ai/mcp``), authenticated with your account API key.
* ``windsock-mcp`` / ``python -m windsock_mcp`` — a stdio bridge so clients that
  only speak stdio can use the remote server.

Docs: https://windsock.ai/mcp
"""

from __future__ import annotations

import os
from contextlib import asynccontextmanager
from typing import AsyncIterator

from mcp import ClientSession
from mcp.client.streamable_http import create_mcp_http_client, streamable_http_client

SERVER_URL = "https://windsock.ai/mcp"

__all__ = ["SERVER_URL", "connect", "headers_for"]


def headers_for(api_key: str | None = None) -> dict[str, str]:
    """Bearer header for the account API key (``WINDSOCK_API_KEY`` if omitted)."""
    key = (api_key or os.environ.get("WINDSOCK_API_KEY", "")).strip()
    if not key:
        raise ValueError(
            "A Windsock API key is required: pass api_key= or set WINDSOCK_API_KEY. "
            "Get one at https://windsock.ai/app/integrations#mcp-agents"
        )
    return {"Authorization": f"Bearer {key}"}


@asynccontextmanager
async def connect(
    api_key: str | None = None, url: str | None = None
) -> AsyncIterator[ClientSession]:
    """Open an initialized :class:`mcp.ClientSession` to the Windsock MCP server.

    Example::

        async with connect() as session:
            tools = await session.list_tools()
            result = await session.call_tool("lookup_aircraft", {"registration": "N12345"})
    """
    server_url = url or os.environ.get("WINDSOCK_MCP_URL", SERVER_URL)
    http_client = create_mcp_http_client(headers=headers_for(api_key))
    async with http_client:
        async with streamable_http_client(server_url, http_client=http_client) as streams:
            read, write = streams[0], streams[1]
            async with ClientSession(read, write) as session:
                await session.initialize()
                yield session
