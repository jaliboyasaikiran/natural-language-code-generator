# Natural Language to Python Code Generator

A Python CLI tool that converts natural-language programming tasks into Python code using a Large Language Model (LLM) through the Groq API.

## Features

- Accepts programming tasks in natural language
- Uses Groq LLM to generate Python code
- Uses a system prompt to request code only
- Removes Markdown code fences if returned by the model
- Displays generated code in the terminal
- Allows the user to choose the output filename
- Automatically adds `.py` extension
- Handles API and file errors

## Technologies Used

- Python
- Groq API
- Python-dotenv
- Large Language Model (LLM)

## Project Structure

```text
natural-language-code-generator/
│
├── agent.py
├── requirements.txt
├── README.md
├── .env
├── .gitignore
│
├── prime_number.py
├── factorial.py
├── reverse_string.py
└── ...