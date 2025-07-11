from langchain_mcp_adapters.client import MultiServerMCPClient
from langgraph.prebuilt import create_react_agent
from langchain_groq import ChatGroq
from dotenv import load_dotenv
load_dotenv()

import asyncio


async def main():
    print("🚀 Starting main...")

    client=MultiServerMCPClient(
        {
            "math":{
                "command":"python",
            "args":["mathserver.py"],   #ensure correct path
            "transport":"stdio",
    

            },
            "weather":{
                "url":"http://localhost:8000/mcp",    
                "transport":"streamable_http",
            }

        }
    )
    print("🔧 Created MultiServerMCPClient")


    import os
    os.environ["GROQ_API_KEY"]=os.getenv("GROQ_API_KEY")
    
    tools=await client.get_tools()
    model=ChatGroq(model="qwen-qwq-32b")
    agent=create_react_agent(
        model,tools
    )

    math_response = await agent.ainvoke({
        "messages":[{"role":"user","content":"what's (10+8)x 2?"}]
    }
    )
   
    print("Math response:",math_response['messages'][-1].content)

    weather_response  = await agent.ainvoke({
        "messages":[{"role":"user","content":
                     "what's weather in Pune?"}]
    }
    )
   
    print("weather_response:", weather_response['messages'][-1].content)

   
    


if __name__ == "__main__":
    asyncio.run(main())