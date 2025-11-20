from interpreter import interpreter
import os
from dotenv import load_dotenv
import asyncio


from fastmcp import FastMCP

load_dotenv()
mcp = FastMCP("open-interpreter")

interpreter.llm.model = os.getenv("MODEL_NAME")
interpreter.llm.api_base = os.getenv("OPENAI_API_BASE")
interpreter.llm.api_key = os.getenv("OPENAI_API_KEY")
interpreter.llm.max_tokens = int(os.getenv("MAX_TOKENS", 3000))
interpreter.llm.context_window = int(os.getenv("CONTEXT_WINDOW", 8000))

# interpreter.system_message += """
# If you need to install any necessary packages, use python3 -m venv venv to create new virtual environment."""
interpreter.auto_run = True
interpreter.verbose = os.getenv("VERBOSE")

@mcp.tool("code_execute")
def code_execute_endpoint(message: str):
    """
    Code as recieved query and execute if needed, finally returns result
    """

    interpreter.messages = []

    full_response = interpreter.chat(message)

    return full_response





# 4. Run the setup and then start the single main server
if __name__ == "__main__":
    
    # Now that the tools are imported, run the main server
    mcp.run(
        host="0.0.0.0",
        port=8000,
        transport="http",
        path="/mcp/open-interpreter"
    )
