#!/usr/bin/env sh
# Claude Code — add Windsock as a remote MCP server (API key; omit --header for OAuth).
claude mcp add --transport http windsock https://windsock.ai/mcp \
  --header "Authorization: Bearer $WINDSOCK_API_KEY"
