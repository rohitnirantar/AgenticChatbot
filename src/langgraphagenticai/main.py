import streamlit as st  # Streamlit for UI
from src.langgraphagenticai.ui.streamlitui.loadui import LoadStreamlitUI  # UI loader
from src.langgraphagenticai.LLMS.groqllm import GroqLLM  # LLM configuration
from src.langgraphagenticai.graph.graph_builder import GraphBuilder  # Graph builder
from src.langgraphagenticai.ui.streamlitui.display_result import DisplayResultStreamlit  # Result display

def load_langgraph_agenticai_app():
    """
    Loads and runs the LangGraph AgenticAI application with Streamlit UI.
    This function initializes the UI, handles user input, configures the LLM model,
    sets up the graph based on the selected use case, and displays the output while 
    implementing exception handling for robustness.
    """

    # Load the Streamlit UI for user controls/input
    ui = LoadStreamlitUI()
    user_input = ui.load_streamlit_ui()

    # If user input is not loaded, show error and exit
    if not user_input:
        st.error("Error: Failed to load user input from the UI.")
        return

    # Get user message from Streamlit chat input
    user_message = st.chat_input("Enter your message:")

    # Proceed only if user has entered a message
    if user_message:
        try:
            # Configure the LLM using user controls/input
            obj_llm_config = GroqLLM(user_contols_input=user_input)
            model = obj_llm_config.get_llm_model()

            # If model initialization fails, show error and exit
            if not model:
                st.error("Error: LLM model could not be initialized")
                return

            # Get the selected use case from user input
            usecase = user_input.get("selected_usecase")

            # If no use case is selected, show error and exit
            if not usecase:
                st.error("Error: No use case selected.")
                return

            # Build the graph for the selected use case
            graph_builder = GraphBuilder(model)
            try:
                # Set up the graph and display the result on the UI
                graph = graph_builder.setup_graph(usecase)
                print(user_message)  # For debugging/logging
                DisplayResultStreamlit(usecase, graph, user_message).display_result_on_ui()
            except Exception as e:
                # Handle errors during graph setup or result display
                st.error(f"Error: Graph set up failed- {e}")
                return

        except Exception as e:
            # Handle errors during LLM configuration or other steps
            st.error(f"Error: Graph set up failed- {e}")
            return
