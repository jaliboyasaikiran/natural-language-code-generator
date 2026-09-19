import os

from dotenv import load_dotenv
from groq import Groq
from groq import APIError


def clean_code(code):
    """Remove Markdown code fences from the generated code."""

    code = code.strip()

    if code.startswith("```python"):
        code = code[len("```python"):].strip()

    elif code.startswith("```"):
        code = code[len("```"):].strip()

    if code.endswith("```"):
        code = code[:-3].strip()

    return code


def generate_code(client, task):
    """Send the task to Groq and return generated Python code."""

    system_prompt = """
You are an expert Python code generator.

Convert the user's natural-language programming task
into correct Python code.

IMPORTANT RULES:

1. Return ONLY Python code.
2. Do NOT provide explanations.
3. Do NOT provide descriptions.
4. Do NOT use Markdown.
5. Do NOT use ```python code fences.
6. Do NOT use ``` code fences.
7. Generate clean, readable and executable Python code.
8. Follow the user's task exactly.
"""

    response = client.chat.completions.create(
        model="openai/gpt-oss-120b",
        messages=[
            {
                "role": "system",
                "content": system_prompt
            },
            {
                "role": "user",
                "content": task
            }
        ],
        temperature=0
    )

    return clean_code(response.choices[0].message.content)


def main():

    # --------------------------------------------------
    # 1. Load .env file
    # --------------------------------------------------

    load_dotenv()

    # --------------------------------------------------
    # 2. Get Groq API key
    # --------------------------------------------------

    api_key = os.getenv("GROQ_API_KEY")

    if not api_key:
        print("\n❌ ERROR: GROQ_API_KEY not found.")
        print("Please check your .env file.")
        return

    # --------------------------------------------------
    # 3. Create Groq client
    # --------------------------------------------------

    client = Groq(api_key=api_key)

    # --------------------------------------------------
    # 4. Display application title
    # --------------------------------------------------

    print("\n" + "=" * 60)
    print("       NATURAL LANGUAGE → PYTHON CODE GENERATOR")
    print("=" * 60)

    # --------------------------------------------------
    # 5. Ask user for coding task
    # --------------------------------------------------

    task = input("\nEnter your coding task:\n> ").strip()

    if not task:
        print("\n❌ ERROR: Task cannot be empty.")
        return

    # --------------------------------------------------
    # 6. Generate code
    # --------------------------------------------------

    print("\n⏳ Generating code...\n")

    try:

        code = generate_code(client, task)

    except APIError as error:

        print("\n❌ Groq API Error:")
        print(error)
        return

    except Exception as error:

        print("\n❌ Unexpected Error:")
        print(error)
        return

    # --------------------------------------------------
    # 7. Display generated code
    # --------------------------------------------------

    print("=" * 60)
    print("                 GENERATED CODE")
    print("=" * 60)

    print(code)

    print("=" * 60)

    # --------------------------------------------------
    # 8. ASK USER FOR FILE NAME
    # --------------------------------------------------

    print("\n")
    filename = input("Enter file name to save the code: ").strip()

    # --------------------------------------------------
    # 9. Check filename
    # --------------------------------------------------

    if not filename:

        print("\n❌ ERROR: File name cannot be empty.")
        return

    # --------------------------------------------------
    # 10. Add .py automatically
    # --------------------------------------------------

    if not filename.lower().endswith(".py"):
        filename = filename + ".py"

    # --------------------------------------------------
    # 11. Check if file already exists
    # --------------------------------------------------

    if os.path.exists(filename):

        print(f"\n⚠️ File '{filename}' already exists.")

        choice = input(
            "Do you want to overwrite it? (y/n): "
        ).strip().lower()

        if choice != "y":

            print("\n❌ File was not saved.")
            return

    # --------------------------------------------------
    # 12. Save generated code
    # --------------------------------------------------

    try:

        with open(filename, "w", encoding="utf-8") as file:
            file.write(code)

        print("\n✓ Code saved successfully!")
        print(f"✓ File: {filename}")

    except OSError as error:

        print("\n❌ Could not save the file.")
        print(error)


# --------------------------------------------------
# Start program
# --------------------------------------------------

if __name__ == "__main__":
    main()