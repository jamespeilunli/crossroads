from prompt_toolkit import prompt
from prompt_toolkit.styles import Style

BOLD = "\x1b[1m"
RESET = "\x1b[0m"

class CLI:
    def __init__(self, client):
        
        self.client = client
        self.paths = [[{"role": "system", "content": "You are a helpful assistant."}], [{"role": "system", "content": "You are a helpful assistant that loves starting words with the letter 'b'."}]]
        self.path_index = 0

    def chat_with_gpt(self, messages):
        response = self.client.chat.completions.create(
            model="gpt-4o-mini",
            messages=messages
        )

        return response.choices[0].message.content

    def process_command(self, user_input):
        parts = user_input[1:].split()
        command = parts[0]
        args = parts[1:]
        if command in {"quit", "q"}:
            quit()
        elif command in {"path", "p"}:
            try:
                new_index = int(args[0])
            except ValueError:
                print(f"{BOLD}Error:{RESET} {new_index} is not an integer")
                return
            if new_index < 0 or new_index >= len(self.paths):
                print(f"{BOLD}Error:{RESET} index {new_index} out of bounds")
                return
            
            self.path_index = new_index
            print(f"Switched to path {self.path_index}")
        else:
            print(f"{BOLD}Error:{RESET} Unknown command \"{command}\"")

    def run(self):
        while True:
            try:
                user_input = prompt(f"Path {self.path_index} Prompt: ", style=Style.from_dict({'prompt': 'bold'}))
                print()

                if user_input[0] == "/":
                    self.process_command(user_input)
                    print()
                else:
                    self.paths[self.path_index].append({"role": "user", "content": user_input})

                    assistant_response = self.chat_with_gpt(self.paths[self.path_index])
                    print(f"{BOLD}Path {self.path_index} Assistant: {RESET}{assistant_response}")
                    print()
                    self.paths[self.path_index].append({"role": "assistant", "content": assistant_response})
            except KeyboardInterrupt:
                quit()
