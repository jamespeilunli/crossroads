import os
from dotenv import load_dotenv
import openai

class OpenAIHandle:
    def __init__(self):
        load_dotenv()
        openai.api_key = os.getenv("OPENAI_API_KEY")

        self.client = openai.OpenAI()
    
    def get_response(self, messages):
        response = self.client.chat.completions.create(
            model="gpt-4o-mini",
            messages=messages
        )
        return response.choices[0].message.content       
        
class Crossroads:
    def __init__(self):
        self.openai_handle = OpenAIHandle()

    def get_response(self, messages):
        return self.openai_handle.get_response(messages)
