// OpenAI Agents API — Windsock as an MCP tool.
// Set WINDSOCK_API_KEY (Integrations → Agents & SDKs) and OPENAI_API_KEY.
import OpenAI from "openai";

const client = new OpenAI();
const session = await client.beta.agents.sessions.create({
  agent: {
    model: "gpt-6-astra",
    tools: [
      {
        type: "mcp",
        server_label: "windsock",
        transport: { type: "http", server_url: "https://windsock.ai/mcp" },
        authorization: process.env.WINDSOCK_API_KEY,
      },
    ],
  },
  input: "What is N12345 worth today, and what should I check before buying it?",
});
console.log(session);
