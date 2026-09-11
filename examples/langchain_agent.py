"""LangChain / LangGraph — Windsock tools via the official MCP adapter.

    pip install langchain-mcp-adapters langchain langgraph langchain-anthropic
    export WINDSOCK_API_KEY=wsk_...     # Integrations → Agents & SDKs
    export ANTHROPIC_API_KEY=...
"""

import asyncio
import os

from langchain_mcp_adapters.client import MultiServerMCPClient


async def main() -> None:
    client = MultiServerMCPClient(
        {
            "windsock": {
                "transport": "streamable_http",
                "url": "https://windsock.ai/mcp",
                "headers": {"Authorization": f"Bearer {os.environ['WINDSOCK_API_KEY']}"},
            }
        }
    )
    tools = await client.get_tools()
    print(f"{len(tools)} Windsock tools loaded:", ", ".join(t.name for t in tools[:6]), "…")

    # Hand them to any LangChain agent, e.g. a LangGraph ReAct agent:
    from langchain_anthropic import ChatAnthropic
    from langgraph.prebuilt import create_react_agent

    agent = create_react_agent(ChatAnthropic(model="claude-opus-5"), tools)
    result = await agent.ainvoke(
        {"messages": [("user", "What is N12345 worth today, and what should I check before buying it?")]}
    )
    print(result["messages"][-1].content)


if __name__ == "__main__":
    asyncio.run(main())
