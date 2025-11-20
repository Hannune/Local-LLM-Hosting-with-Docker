# client.py (Ensure this version is used)
import asyncio
from langchain_mcp_adapters.client import MultiServerMCPClient

client = MultiServerMCPClient(
    {
        "combined_tools": {
            "url": "http://localhost:8000/mcp/open-interpreter",
            "transport": "streamable_http",
        },
    }
)

async def main():
    tools = await client.get_tools()
    print(tools)
    tool_map = {tool.name: tool for tool in tools}

    print("--- Available Tools ---")
    for tool_name in tool_map:
        # This will print the actual names the server exposes (e.g., 'add', 'get_weather')
        print(f"Tool: {tool_name}") 


    query = "print Hello"

    
    print("\n" + "-"*50)
    tool_name = "code_execute" # FIX: Use simple name
    print(f"Invoking tool: {tool_name}")
    if tool_name in tool_map:
        res = await tool_map[tool_name].ainvoke(input={"message": query})
        print(f"Result: {res}")
    else:
        print(f"Tool {tool_name} not found.")



    print("\n" + "-"*50)


if __name__ == "__main__":
    asyncio.run(main())