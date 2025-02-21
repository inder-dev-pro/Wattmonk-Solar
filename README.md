# Wattmonk-Solar

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