import httpx
from mcp.server.fastmcp import FastMCP
from config.config import Config


# Create MCP server
internet_mcp = FastMCP("Internet_Tool")


@internet_mcp.tool()
def search_web(query: str) -> str:
    """
    Search the web using Serper API and return the top result.
    """
    url = "https://google.serper.dev/search"
    headers = {
        "X-API-KEY": Config.SERPER_API_KEY,
        "Content-Type": "application/json"
    }
    payload = {"q": query}

    try:
        response = httpx.post(url, headers=headers, json=payload)
        response.raise_for_status()
        results = response.json()
        if results.get("organic"):
            top_result = results["organic"][0]
            return f"Top result: {top_result['title']} - {top_result['link']}\n{top_result['snippet']}"
        else:
            return "No search results found."
    except Exception as e:
        return f"Error while searching: {str(e)}"


if __name__ == "__main__":
    internet_mcp.run()
    # query = "Upcoming bollywood movie in 2026"
    # print(search_web(query))

    

