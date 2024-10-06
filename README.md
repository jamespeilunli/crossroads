# Crossroads

ChatGPT-powered chatbot supporting multiple conversation paths

Very WIP.

## Running the CLI

### Setup

Write a .env with your OpenAI API key in it:
```
OPENAI_API_KEY=sk-proj-XXXXXXXXXXXXXXXXXXXXXXX
```

### Run with a virtual environment (recommended)

```bash
python -m venv venv
source ./venv/bin/activate
pip install -r cli/requirements.txt
python -m cli.main
```
Use Ctrl+D to quit the program.

Leave the virtual environment:
```bash
deactivate
```

## Using the CLI

Conversations between you and the chatbot are stored as **paths**. Each path is an ordered collection of back and forth message exchanges, and each exchange has a **timestamp**. Every time you chat with the chatbot, the CLI will add your message and the chatbot's response to the current path, with a new timestamp.

### Commands

Instead of prompting the chatbot, you can also run commands, which are always prefixed by "/". Arguments passed to the command are separated by spaces. Some commands are:
* `/quit`
* `/list_timestamps`
* `/list_paths`
* `/set_path i` (changes the current path to path `i`)
* `/new_path i` (creates a new path at timestamp `i` and sets the current path to it)
* `/last` (prints the latest assistant message in the path)

## Running the web app locally

Compile:
```bash
cd web
npx tailwindcss -i static/styles/* -o static/styles/tailwind.css # use --watch to dynamically update
cd .. # go back to root of repo
```

Install dependencies:
```bash
python -m venv venv
source ./venv/bin/activate
pip install -r web/requirements.txt
```

Start local server:
```bash
python3 -m web.app
```
