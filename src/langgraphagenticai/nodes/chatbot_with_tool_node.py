from src.langgraphagenticai.state.state import State

class ChatbotWithToolNode():
    """
    Chatbot logic enhanced with tool integration
    """
    def __init__(self,model):
        self.llm = model

    def process(self,state:State)->dict:
        """
        Processes the input state and generates a response with tool integration.
        """
        user_input = state['messages'][-1].content if state.get('messages') else ""
        llm_response = self.llm.invoke([{"role":"user","content":user_input}])

        # simulate tool-specific logic
        tool_response = f"Tool integration for: '{user_input}'"

        return {"messages": [llm_response, tool_response]}
    
    def create_chatbot(self,tools):
        """"
        Return a chatbot node function
        """
        llm_with_tool = self.llm.bind_tools(tools)

        def chatbot_node(state:State):
            """
            Chatbot logic for processing the input state and returning a response
            """
            # Convert message objects to dicts with 'role' and 'content'
            messages = state['messages']
            formatted_messages = []
            for msg in messages:
                if hasattr(msg, 'role') and hasattr(msg, 'content'):
                    formatted_messages.append({"role": msg.role, "content": msg.content})
                else:
                    # fallback: treat as user message
                    formatted_messages.append({"role": "user", "content": str(msg)})
            llm_output = llm_with_tool.invoke(formatted_messages)
            print(f"Chatbot Node Output: {llm_output}")  # Inspect the output
            return {"messages": llm_output}

        return chatbot_node