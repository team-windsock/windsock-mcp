# windsock-mcp

Windsock aircraft intelligence for AI agents, as a stdio MCP server.

[Windsock](https://windsock.ai) exposes 38 tools over the Model Context Protocol:
aircraft valuations, FAA registry lookups (US N-numbers and 17 international
registers), cost of ownership, comparable aircraft, fleet search, ADs and STCs,
market metrics with forecasts, verified value reports, pre-buy diligence
checklists, logbook search and a watchlist. The remote server lives at
`https://windsock.ai/mcp`; this package is a thin stdio bridge for clients that
don't connect to remote servers directly.

## Install

```json
{
  "mcpServers": {
    "windsock": {
      "command": "npx",
      "args": ["-y", "windsock-mcp"]
    }
  }
}
```

That's it for Claude Desktop, Cursor, Windsurf, VS Code and Zed. The first run
opens the Windsock sign-in and consent screen in your browser (OAuth); after
that the bridge refreshes tokens on its own.

### Headless / CI: API key instead of OAuth

```json
{
  "mcpServers": {
    "windsock": {
      "command": "npx",
      "args": ["-y", "windsock-mcp"],
      "env": { "WINDSOCK_API_KEY": "wsk_…" }
    }
  }
}
```

Get a key from **Integrations → Agents & SDKs** in your Windsock account.
Treat it like a password.

## Plans

Free accounts get 20 of the 38 tools with a monthly call limit. Pro and
Enterprise unlock reports, diligence, logbooks and tracking.

## Docs

- Developer docs, full tool catalog, limits and errors: https://windsock.ai/mcp
- Setup walkthroughs for ChatGPT, Claude and Grok: https://windsock.ai/ai-assistants
- Machine-readable: https://windsock.ai/mcp/llms.txt

## License

MIT © Windsock

<!-- The official MCP Registry uses this line to verify package ownership. -->
mcp-name: ai.windsock/windsock
