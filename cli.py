from prompt_toolkit import prompt
from prompt_toolkit.styles import Style

BOLD = "\x1b[1m"
RESET = "\x1b[0m"

class CLI:
    def __init__(self, client):
        
        self.client = client
        self.paths = [[{"role": "system", "content": "You are a helpful assistant."}], [{"role": "system", "content": "You are a helpful assistant that loves starting words with the letter 'b'."}]]
        self.path_index = 0
        self.timestamp = 0

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
        elif command in {"newpath", "new", "n"}:
            if len(args) == 0:
                self.paths.append(self.paths[self.path_index][:])
                old_path_index = self.path_index
                self.path_index = len(self.paths) - 1
                print(f"Switched to new path {self.path_index} at latest timestamp of old path {old_path_index}")
            else:
                try:
                    self.timestamp = int(args[0])
                except ValueError:
                    print(f"{BOLD}Error:{RESET} {self.timestamp} is not an integer")
                    return
                if self.timestamp < 0 or self.timestamp >= len(self.paths[self.path_index]) // 2:
                    print(f"{BOLD}Error:{RESET} index {self.timestamp} out of bounds")
                    return

                self.paths.append(self.paths[self.path_index][:2*(self.timestamp+1)])
                old_path_index = self.path_index
                self.path_index = len(self.paths) - 1
                print(f"Switched to new path {self.path_index} at timestamp {self.timestamp} of old path {old_path_index}")
        else:
            print(f"{BOLD}Error:{RESET} Unknown command \"{command}\"")

    def run(self):
        while True:
            try:
                user_input = prompt(f"Path {self.path_index} Time {self.timestamp} Prompt: ", style=Style.from_dict({'prompt': 'bold'}))
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

                    self.timestamp += 1
            except KeyboardInterrupt:
                quit()
