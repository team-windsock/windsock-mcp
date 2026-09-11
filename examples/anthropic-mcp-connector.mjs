// Anthropic Messages API — Windsock via the MCP connector.
// Set WINDSOCK_API_KEY (Integrations → Agents & SDKs) and ANTHROPIC_API_KEY.
import Anthropic from "@anthropic-ai/sdk";

const client = new Anthropic();
const response = await client.beta.messages.create({
  model: "claude-opus-5",
  max_tokens: 16000,
  betas: ["mcp-client-2025-11-20"],
  mcp_servers: [
    {
      type: "url",
      name: "windsock",
      url: "https://windsock.ai/mcp",
      authorization_token: process.env.WINDSOCK_API_KEY,
    },
  ],
  tools: [{ type: "mcp_toolset", mcp_server_name: "windsock" }],
  messages: [{ role: "user", content: "What is N12345 worth today?" }],
});
for (const block of response.content) {
  if (block.type === "text") console.log(block.text);
}
