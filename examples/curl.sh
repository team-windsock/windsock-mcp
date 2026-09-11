#!/usr/bin/env sh
# List the tools your account can see.
curl -sS https://windsock.ai/mcp \
  -H "Authorization: Bearer $WINDSOCK_API_KEY" \
  -H "Content-Type: application/json" \
  -H "Accept: application/json, text/event-stream" \
  -d '{"jsonrpc":"2.0","id":1,"method":"tools/list"}'
