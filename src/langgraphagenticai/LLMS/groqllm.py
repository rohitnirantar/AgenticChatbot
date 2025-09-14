
# Import required modules
import os
import streamlit as st  # For UI error display
from langchain_groq import ChatGroq  # Groq LLM integration

class GroqLLM:
    """
    Class to handle Groq LLM configuration and instantiation.
    """
    def __init__(self, user_contols_input):
        # Store user controls/input for LLM configuration
        self.user_controls_input = user_contols_input

    def get_llm_model(self):
        """
        Initializes and returns a Groq LLM model based on user input.
        Handles missing API key and model selection errors.
        """
        try:
            # Retrieve API key and model selection from user input
            groq_api_key = self.user_controls_input["GROQ_API_KEY"]
            selected_groq_model = self.user_controls_input["selected_groq_model"]

            # Check if API key is provided either via input or environment variable
            if groq_api_key == '' and os.environ["GROQ_API_KEY"] == '':
                st.error("Please Enter the Groq API KEY")

            # Instantiate the Groq LLM model
            llm = ChatGroq(api_key=groq_api_key, model=selected_groq_model)

        except Exception as e:
            # Raise a ValueError with details if any error occurs
            raise ValueError(f"Error Ocuured With Exception : {e}")
        return llm