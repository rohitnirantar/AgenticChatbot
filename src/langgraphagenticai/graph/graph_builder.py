
# Import required modules and classes
from langgraph.graph import StateGraph  # For building stateful graphs
from src.langgraphagenticai.state.state import State  # Custom state definition
from langgraph.graph import START, END  # Special graph markers
from src.langgraphagenticai.nodes.basic_chatbot_node import BasicChatbotNode  # Chatbot node logic



class GraphBuilder:
    """
    Class responsible for building and compiling LangGraph graphs for different use cases.
    """
    def __init__(self, model):
        # Store the LLM model instance
        self.llm = model
        # Initialize the stateful graph with the custom State class
        self.graph_builder = StateGraph(State)

    def basic_chatbot_build_graph(self):
        """
        Builds a basic chatbot graph using LangGraph.
        This method initializes a chatbot node using the `BasicChatbotNode` class 
        and integrates it into the graph. The chatbot node is set as both the 
        entry and exit point of the graph.
        """

        # Create a basic chatbot node with the LLM
        self.basic_chatbot_node = BasicChatbotNode(self.llm)

        # Add the chatbot node to the graph
        self.graph_builder.add_node("chatbot", self.basic_chatbot_node.process)
        # Set the start and end edges for the graph
        self.graph_builder.add_edge(START, "chatbot")
        self.graph_builder.add_edge("chatbot", END)

    def setup_graph(self, usecase: str):
        """
        Sets up the graph for the selected use case.
        Currently supports only the 'Basic Chatbot' use case.
        Returns the compiled graph ready for execution.
        """
        # Check which use case is selected and build the corresponding graph
        if usecase == "Basic Chatbot":
            self.basic_chatbot_build_graph()

        # Compile and return the graph
        return self.graph_builder.compile()
