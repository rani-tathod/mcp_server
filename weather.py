from mcp.server.fastmcp import FastMCP

mcp=FastMCP("Weather")

@mcp.tool()
async def get_weather(location:str)->str:
    """get the weather location"""
    return "Its always raining in Pune"


if __name__=="__main__":
    mcp.run(transport="streamable-http")  # uses the url as api
    