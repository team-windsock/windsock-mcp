"""``windsock-mcp`` — stdio bridge to the remote Windsock MCP server.

Forwards ``tools/list`` and ``tools/call`` from a stdio client to
``https://windsock.ai/mcp`` using the account API key in ``WINDSOCK_API_KEY``.
For interactive OAuth use prefer the npm bridge (``npx windsock-mcp``), which
handles the browser consent flow.
"""

from __future__ import annotations

import asyncio
import sys

import mcp.types as types
from mcp import stdio_server
from mcp.server import Server

from . import connect


async def _serve() -> None:
    async with connect() as upstream:

        async def on_list_tools(_ctx, params):
            return await upstream.list_tools(cursor=params.cursor if params else None)

        async def on_call_tool(_ctx, params: types.CallToolRequestParams):
            return await upstream.call_tool(params.name, params.arguments or {})

        server: Server = Server(
            "windsock",
            website_url="https://windsock.ai/mcp",
            on_list_tools=on_list_tools,
            on_call_tool=on_call_tool,
        )
        async with stdio_server() as (read, write):
            await server.run(read, write, server.create_initialization_options())


def main() -> None:
    try:
        asyncio.run(_serve())
    except ValueError as err:  # missing key
        print(f"windsock-mcp: {err}", file=sys.stderr)
        sys.exit(2)
    except KeyboardInterrupt:
        pass


if __name__ == "__main__":
    main()
