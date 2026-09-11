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
| Examples | [`examples/`](examples/) — OpenAI Agents API, Anthropic MCP connector, LangChain, LlamaIndex, Claude Code, cURL |
| Listed on | [Smithery](https://smithery.ai/servers/team-3go2/windsock) · official MCP Registry `ai.windsock/windsock` · ChatGPT app |

## One-click install

[![Install in VS Code](https://img.shields.io/badge/VS_Code-Install_Windsock-0098FF?style=flat-square&logo=visualstudiocode&logoColor=white)](vscode:mcp/install?%7B%22name%22%3A%20%22windsock%22%2C%20%22type%22%3A%20%22http%22%2C%20%22url%22%3A%20%22https%3A%2F%2Fwindsock.ai%2Fmcp%22%7D)
[![Install in VS Code Insiders](https://img.shields.io/badge/VS_Code_Insiders-Install_Windsock-24bfa5?style=flat-square&logo=visualstudiocode&logoColor=white)](vscode-insiders:mcp/install?%7B%22name%22%3A%20%22windsock%22%2C%20%22type%22%3A%20%22http%22%2C%20%22url%22%3A%20%22https%3A%2F%2Fwindsock.ai%2Fmcp%22%7D)
[![Install in Cursor](https://img.shields.io/badge/Cursor-Install_Windsock-000000?style=flat-square)](cursor://anysphere.cursor-deeplink/mcp/install?name=windsock&config=eyJ1cmwiOiAiaHR0cHM6Ly93aW5kc29jay5haS9tY3AifQ==)

Claude Code:

```bash
claude mcp add --transport http windsock https://windsock.ai/mcp
```

or install the plugin (adds the server plus an aircraft pre-buy workflow skill; the repo root follows the [Open Plugins](https://open-plugins.com) layout, so Cursor and other Open Plugins clients can import it too):

```
/plugin marketplace add team-windsock/windsock-mcp
/plugin install windsock@windsock
```

Every client above signs you in with OAuth on first use. Headless agents use an API key instead — see the docs.

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
