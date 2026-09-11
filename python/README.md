# windsock-mcp

Windsock aircraft intelligence for AI agents, from Python.

[Windsock](https://windsock.ai) exposes 38 tools over the Model Context Protocol
at `https://windsock.ai/mcp`: aircraft valuations, FAA registry lookups, cost of
ownership, comparable aircraft, fleet search, ADs and STCs, market metrics with
forecasts, verified value reports, pre-buy diligence checklists, logbook search
and a watchlist. This package gives you a client helper and a stdio bridge.

```bash
pip install windsock-mcp
export WINDSOCK_API_KEY=wsk_…   # Integrations → Agents & SDKs in your Windsock account
```

## Call tools directly

```python
import asyncio
from windsock_mcp import connect

async def main():
    async with connect() as session:
        tools = await session.list_tools()
        print([t.name for t in tools.tools])
        result = await session.call_tool("lookup_aircraft", {"registration": "N12345"})
        print(result.content[0].text)

asyncio.run(main())
```

## Use as a stdio MCP server

```json
{
  "mcpServers": {
    "windsock": {
      "command": "windsock-mcp",
      "env": { "WINDSOCK_API_KEY": "wsk_…" }
    }
  }
}
```

## Docs

- https://windsock.ai/mcp — endpoint, auth, quickstarts, full tool catalog
- https://windsock.ai/mcp/llms.txt — machine-readable index

MIT © Windsock

<!-- The official MCP Registry uses this line to verify package ownership. -->
mcp-name: ai.windsock/windsock
