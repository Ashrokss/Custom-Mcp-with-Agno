
import nest_asyncio
from config.config import Config
import asyncio
from agno.agent import Agent
from agno.tools.mcp import MCPTools
from agno.models.groq import Groq
import warnings
warnings.filterwarnings("ignore", category=ResourceWarning)

# Allow nested event loops
nest_asyncio.apply()


async def run_agent(query: str):

    # async with MCPTools("npx -y firecrawl-mcp") as mcp_tools2:
    async with MCPTools("python mcp_server.py") as mcp_tools2:

        try:
            agent = Agent(model=Groq(id="meta-llama/llama-4-scout-17b-16e-instruct", api_key=Config.GROQ_API_KEY),
                          tools=[mcp_tools2], markdown=True, show_tool_calls=True, debug_mode=True)
            await agent.aprint_response(query, stream=True)

        except Exception as ex:
            print(ex)


if __name__ == "__main__":
    query = input("Query: ")
    asyncio.run(run_agent(query))
