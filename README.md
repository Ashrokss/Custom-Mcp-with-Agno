# Custom‑MCP with Agno

This repository demonstrates how to build a custom **Model Context Protocol (MCP)** server and client using the **Agno** agent framework. It features:

* ✅ A working **MCP server** (custom tool implementations)
* ✅ A Python **MCP client** powered by **Agno / AnyIO / agno.tools**
* ✅ Example agent workflows, handling tool calls and async management
* ✅ Clean sample architecture with minimal dependencies

---

## 📘 Architecture

```
┌──────────────┐           ┌──────────────┐           ┌───────────────┐
│ MCP Server   │<—→ SSE / HTTP —›│ Agno Agent  │<— Tool Calls —›│ Tools / LLM    │
└──────────────┘           └──────────────┘           └───────────────┘
```

1. **MCP server (`mcp_server.py`)**: serves tool endpoints, e.g. web search.
2. **Client (`mcp_client.py`)**: agent-side runner using `agno.tools.MCPTools`
3. **Agent logic**: handles queries, invokes tools, and processes results.

---

##  Features

* Asynchronous context management via `anyio` and `async with MCPTools(...)`.
* Agent retries and error handling (including handling “no space left on device” issues).
* Template for adding new tools or extending MCP interface.
* Example agent running loop included in `mcp_client.py`.

---



## 📁 Code Structure

| File               | Description                                                     |
| ------------------ | -------------------------------------------------------         |
| `mcp_server.py`    | Python MCP server with sample tool implementations              |
| `mcp_client.py`    | Agent client to issue queries and handle agent response         |
| `requirements.txt` | Python dependencies: `agno`, `anyio`, etc.                      |
| `.venv/`           | (Optional) Virtual environment directory                        |
| `config/config`    | Environment Variables such as `SERPER_API_KEY` & `GROQ_API_KEY` |

---

### 🔑 Set Up Configuration

In `config.py`, define:

```python
class Config:
    GROQ_API_KEY = "<your_groq_api_key>"
    SERPER_API_KEY = "<your_serper_api_key>"
```

