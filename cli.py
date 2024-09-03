from prompt_toolkit import prompt
from prompt_toolkit.styles import Style
from prompt_toolkit.application import get_app

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

    def get_terminal_width(self):
        app = get_app()
        if app.output:
            return app.output.get_size().columns
        return 80 # default fallback width

    def _list_paths(self, args):
        print("Paths:")
        for i, path in enumerate(self.paths):
            content = path[-1]["content"]
            if i == self.path_index:
                print(BOLD + f"{i} {content}"[:self.get_terminal_width()] + RESET)
            else:
                print(f"{i} {content}"[:self.get_terminal_width()])
            
    def _set_path(self, args):
        try:
            new_index = int(args[0])
        except ValueError:
            print(f"{BOLD}Error:{RESET} {new_index} is not an integer")
            return
        except IndexError:
            print("No arguments passed to set_path. Running list_paths instead.")
            self._list_paths(args)
            return
        if new_index < 0 or new_index >= len(self.paths):
            print(f"{BOLD}Error:{RESET} index {new_index} out of bounds")
            return
        
        self.path_index = new_index
        print(f"Switched to path {self.path_index}")

    def _new_path(self, args):
        if len(args) == 0:
            self.paths.append(self.paths[self.path_index][:])
            old_path_index = self.path_index
            self.path_index = len(self.paths) - 1
            print(f"Switched to new path {self.path_index} at latest timestamp of old path {old_path_index}")
        else:
            try:
                timestamp = int(args[0])
            except ValueError:
                print(f"{BOLD}Error:{RESET} {timestamp} is not an integer")
                return
            if timestamp < 0 or timestamp >= len(self.paths[self.path_index]) // 2:
                print(f"{BOLD}Error:{RESET} timestamp {timestamp} out of bounds")
                return

            self.timestamp = timestamp
            self.paths.append(self.paths[self.path_index][:2*(self.timestamp+1)])
            old_path_index = self.path_index
            self.path_index = len(self.paths) - 1
            print(f"Switched to new path {self.path_index} at timestamp {self.timestamp} of old path {old_path_index}")

    def process_command(self, user_input):
        parts = user_input[1:].split()
        command = parts[0]
        args = parts[1:]
        if command in {"quit", "q"}:
            quit()
        elif command in {"list_paths", "lp"}:
            self._list_paths(args)
        elif command in {"set_path", "sp"}:
            self._set_path(args)
        elif command in {"new_path", "np"}:
            self._new_path(args)
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
