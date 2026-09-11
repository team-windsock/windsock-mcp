# Windsock MCP

Aircraft intelligence for AI agents. [Windsock](https://windsock.ai) exposes 38
tools over the Model Context Protocol at `https://windsock.ai/mcp`: aircraft
valuations, FAA registry lookups (US and 17 international registers), cost of
ownership, comparable aircraft, fleet search, ADs and STCs, market metrics with
forecasts, verified value reports, pre-buy diligence checklists, logbook search
and a watchlist. Every call is tied to a Windsock account.

This repository holds the client packages and examples. The server itself is
hosted; you never run it.

| | |
|---|---|
| Docs | https://windsock.ai/mcp |
| npm bridge (stdio, OAuth or API key) | [`npm/`](npm/) → `npx windsock-mcp` |
| Python client + stdio bridge | [`python/`](python/) → `pip install windsock-mcp` |
| Examples | [`examples/`](examples/) — OpenAI Agents API, Anthropic MCP connector, Claude Code, cURL |
| Listed on | [Smithery](https://smithery.ai/servers/team-3go2/windsock) · official MCP Registry `ai.windsock/windsock` · ChatGPT app |

## Quick start (any MCP client)

Remote server, no install:

```
https://windsock.ai/mcp
```

Chat assistants connect over OAuth. Agents send an account API key as
`Authorization: Bearer wsk_…` (get one at **Integrations → Agents & SDKs**).

## Plans

Free accounts get 20 of the 38 tools with a monthly call limit. Pro and
Enterprise unlock reports, diligence, logbooks and tracking.

## Support

support@windsock.ai · https://windsock.ai/contact

MIT © Windsock
