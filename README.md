MCP AI Agent (Math + Weather)

This project shows how to build an AI assistant that can:

🧮 Do math using a tool server (add, multiply)

🌦️ Get weather info using another tool server

It uses:

mathserver.py → 
math tools via stdio ,

weatherserver.py → 
weather tool via HTTP API,

client.py → 
connects both using LangChain + Groq model

🔧 Requirements:

Python 3.8+

pip install -r requirements.txt

Add .env file insdie add groq API Key

GROQ_API_KEY=your_groq_api_key

▶️ How to Run

Run mathserver.py in one terminal:  

  python mathserver.py

Run weather.py in another:

  python weather.py

Run the main client:

  python client.py

✅ Output Example

Math response: The result is 36
weather_response: Its always raining in Pune

Summary
This project shows:
How to connect multiple external tools to an AI agent
Use of LangChain, Groq model, and MCP (Multi-Component Protocol)
