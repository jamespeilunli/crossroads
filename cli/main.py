import os
from dotenv import load_dotenv
import openai

from cli import CLI

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

client = openai.OpenAI()

cli = CLI(client)
cli.run()

