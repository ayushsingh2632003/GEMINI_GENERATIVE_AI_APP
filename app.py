from dotenv import load_dotenv
import streamlit as st
import os
from google import generativeai as genai

# Load environment variables
load_dotenv()

# Configure generative AI
try:
    genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))
except Exception as e:
    st.error(f"Error configuring generative AI: {str(e)}")

# Define generative model
model = genai.GenerativeModel('gemini-pro')

# Function to get Gemini response
def get_gemini_response(question):
    with st.spinner("Generating response..."):
        response = model.generate_content(question)
    return response.text if response is not None else None

# Streamlit UI IO
st.set_page_config(page_title="Q n A DEMO")
st.header("Gemini LLM application")
input_question = st.text_input("Input: ", key="input")
submit_button = st.button("Ask  GEMINI")

if submit_button:
    if not input_question:
        st.warning("Please enter a question.")
    else:
        response = get_gemini_response(input_question)
        if response is not None:
            st.subheader("GEMINI SAYS >>>")
            st.write(response)
        else:
            st.error("Sorry, there was an issue generating a response. Please try again.")
