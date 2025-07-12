from langchain_community.tools.tavily_search.tool import TavilySearchResults
from langchain_tavily.tavily_search import TavilySearch
from langgraph.prebuilt import ToolNode

def get_tools():
    """
    Return the list of tools to be used in the chatbot
    """
    tools = [TavilySearchResults(max_results=2)]
    return tools

def create_tool_node(tools):
    """
    create and return a tool node for the graph
    """
    return ToolNode(tools=tools)