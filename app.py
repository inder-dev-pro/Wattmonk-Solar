# Directory structure:
# solar_assistant/
# ├── app.py
# ├── requirements.txt
# ├── config.py
# ├── src/
# │   ├── __init__.py
# │   ├── assistant.py
# │   ├── prompts.py
# │   └── utils.py
# └── README.md


# config.py
import os
from dotenv import load_dotenv

load_dotenv()

GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
MODEL = "gemini-pro"
# app.py
import streamlit as st
from src import SolarAssistant, format_response, validate_input

st.set_page_config(
    page_title="Solar Industry Assistant",
    page_icon="☀️",
    layout="wide"
)

if "assistant" not in st.session_state:
    st.session_state.assistant = SolarAssistant()

st.title("☀️ Solar Industry Assistant")
st.markdown("""
Get expert guidance on solar technology, installation, maintenance, costs, and regulations.
""")

user_input = st.text_area("Ask your question:", height=100)

col1, col2, col3 = st.columns([1, 1, 4])
with col1:
    if st.button("Send", use_container_width=True):
        if validate_input(user_input):
            with st.spinner("Thinking..."):
                response = st.session_state.assistant.get_response(user_input)
                st.markdown(format_response(response), unsafe_allow_html=True)
        else:
            st.error("Please enter a question.")

with col2:
    if st.button("Clear Chat", use_container_width=True):
        st.session_state.assistant.clear_history()
        st.experimental_rerun()

# README.md
# Solar Industry AI Assistant

An AI-powered assistant specializing in solar industry consulting, providing expert guidance on solar technology, installation, maintenance, costs, and regulations.

## Setup Instructions

1. Clone the repository
2. Create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Create a `.env` file with your Google API key:
   ```
   GOOGLE_API_KEY=your_api_key_here
   ```
5. Run the application:
   ```bash
   streamlit run app.py
   ```

## Features

- Real-time AI responses to solar industry queries
- Conversation history management
- Clean, intuitive web interface
- Expert knowledge in:
  - Solar panel technology
  - Installation processes
  - Maintenance requirements
  - Cost & ROI analysis
  - Industry regulations
  - Market trends

## Development Notes

- Built with Streamlit for rapid deployment
- Uses Google's Generative AI (Gemini Pro) for AI capabilities
- Implements conversation management
- Includes input validation and response formatting
- Modular architecture for easy maintenance and scaling