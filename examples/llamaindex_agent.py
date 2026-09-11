"""LlamaIndex — Windsock tools via the official MCP tool spec.

    pip install llama-index-tools-mcp llama-index llama-index-llms-anthropic
    export WINDSOCK_API_KEY=wsk_...     # Integrations → Agents & SDKs
    export ANTHROPIC_API_KEY=...
"""

import asyncio
import os

from llama_index.tools.mcp import BasicMCPClient, McpToolSpec


async def main() -> None:
    client = BasicMCPClient(
        "https://windsock.ai/mcp",
        headers={"Authorization": f"Bearer {os.environ['WINDSOCK_API_KEY']}"},
    )
    tools = await McpToolSpec(client=client).to_tool_list_async()
    print(f"{len(tools)} Windsock tools loaded:", ", ".join(t.metadata.name for t in tools[:6]), "…")

    # Hand them to any LlamaIndex agent:
    from llama_index.core.agent.workflow import FunctionAgent
    from llama_index.llms.anthropic import Anthropic

    agent = FunctionAgent(tools=tools, llm=Anthropic(model="claude-opus-5"))
    response = await agent.run("What is N12345 worth today, and what should I check before buying it?")
    print(str(response))


if __name__ == "__main__":
    asyncio.run(main())
