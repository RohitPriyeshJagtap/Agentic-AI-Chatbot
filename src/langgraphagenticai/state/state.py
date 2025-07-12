from typing_extensions import TypedDict
from typing import Annotated
from langgraph.graph.message import add_messages
from langchain_core.messages import AnyMessage

class State(TypedDict):
    """State with message history that appends new chat messages."""
    messages: Annotated[list[AnyMessage], add_messages]
