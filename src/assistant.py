import google.generativeai as genai
from .prompts import SYSTEM_PROMPT
import config
class SolarAssistant:
    def __init__(self):
        genai.configure(api_key=config.GOOGLE_API_KEY)
        self.model = genai.GenerativeModel(config.MODEL)
        self.conversation = self.model.start_chat(history=[])
        self.prime_assistant()
    
    def prime_assistant(self):
        self.conversation.send_message(SYSTEM_PROMPT)
    
    def get_response(self, user_input):
        response = self.conversation.send_message(user_input)
        return response.text

    def clear_history(self):
        self.conversation = self.model.start_chat(history=[])
        self.prime_assistant()