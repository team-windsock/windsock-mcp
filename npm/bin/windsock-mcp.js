#!/usr/bin/env node
// windsock-mcp — stdio bridge to the Windsock MCP server (https://windsock.ai/mcp).
//
// Lets MCP clients that only speak stdio (Claude Desktop, Cursor, Windsurf, VS Code,
// Zed, …) use Windsock. Two modes:
//
//   1. OAuth (default): opens the Windsock consent screen in your browser the first
//      time and refreshes tokens after that. Just run `npx windsock-mcp`.
//   2. API key: set WINDSOCK_API_KEY=wsk_… (from windsock.ai/app/integrations, the
//      "Agents & SDKs" panel) and the bridge sends it as a bearer header — no browser.
//
// Everything is delegated to mcp-remote; this wrapper only pins the server URL
// and wires the header. Docs: https://windsock.ai/mcp
import { spawn } from "node:child_process";
import { createRequire } from "node:module";

const SERVER_URL = process.env.WINDSOCK_MCP_URL || "https://windsock.ai/mcp";
const apiKey = (process.env.WINDSOCK_API_KEY || "").trim();

const args = [SERVER_URL, "--transport", "http-only"];
if (apiKey) args.push("--header", `Authorization: Bearer ${apiKey}`);
// Pass through any extra flags (e.g. --debug) to mcp-remote.
args.push(...process.argv.slice(2));

const require = createRequire(import.meta.url);
let entry;
try {
  entry = require.resolve("mcp-remote/dist/proxy.js");
} catch {
  console.error("windsock-mcp: mcp-remote is not installed. Run `npm install -g windsock-mcp`.");
  process.exit(1);
}

const child = spawn(process.execPath, [entry, ...args], { stdio: "inherit" });
child.on("exit", (code, signal) => {
  if (signal) process.kill(process.pid, signal);
  process.exit(code ?? 0);
});
for (const sig of ["SIGINT", "SIGTERM"]) {
  process.on(sig, () => child.kill(sig));
}
