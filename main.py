import os
from dotenv import load_dotenv
import openai
from prompt_toolkit import prompt

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

client = openai.OpenAI()

def chat_with_gpt(messages):
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=messages
    )

    return response.choices[0].message.content

def main():
    messages = [{"role": "system", "content": "You are a helpful assistant."}]
    
    while True:
        try:
            user_input = prompt('Prompt: ')
            messages.append({"role": "user", "content": user_input})
            print()

            assistant_response = chat_with_gpt(messages)
            print(f"Assistant: {assistant_response}")
            messages.append({"role": "assistant", "content": assistant_response})
            print()
        except KeyboardInterrupt:
            quit()

if __name__ == "__main__":
    main()

