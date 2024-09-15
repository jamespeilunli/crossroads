import os
from dotenv import load_dotenv
import openai

class OpenAIHandle:
    def __init__(self):
        load_dotenv()
        openai.api_key = os.getenv("OPENAI_API_KEY")

        self.client = openai.OpenAI()
    
    def get_response(self, messages):
        """
        get the response of the LLM as a stream
        """
        response = self.client.chat.completions.create(
            model='gpt-4o-mini',
            messages=messages,
            stream=True
        )

        for chunk in response:
            message_chunk = chunk.choices[0].delta.content
            if message_chunk is not None:
                yield message_chunk
    
    def list_models(self):
        """
        lists the availiable models from OpenAI
        can be used as a no-cost test to check if API key works
        """
        models = self.client.models.list()
        model_list = [model.id for model in models]
        return model_list

class Crossroads:
    def __init__(self):
        self.openai_handle = OpenAIHandle()

    def get_response(self, messages):
        return self.openai_handle.get_response(messages)
    
    def list_models(self):
        return self.openai_handle.list_models()
