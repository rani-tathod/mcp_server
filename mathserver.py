from mcp.server.fastmcp import FastMCP

mcp=FastMCP("Math")

@mcp.tool()
def add(a:int,b:int)->int:
    """_summary_
    """
    return a+b

@mcp.tool()
def multiply(a: int, b: int) -> int:
    """Multiply two numbers"""
    return a * b


if __name__=="__main__":
    mcp.run(transport="stdio")   # stdio tells the server to use standard i/o to receiv 
    #and respond to tool function calls 