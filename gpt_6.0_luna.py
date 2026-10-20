from openai import OpenAI

client = OpenAI()

# Model Name

MODEL = "gpt-6-luna"

# Special Instructions

INSTRUCTIONS = """
You are a helpful AI assistant.
Give clear, accurate answers.
If you are unsure about something, say so.
"""
# For Visual Representation

print("=" * 40)
print("       AI CHATBOT")
print("=" * 40)

# Quit Instructions

print("Type 'exit' to quit.\n")

# Structure Of Messages

while True:
    user_message = input("You: ").strip()

    if user_message.lower() == "exit":
        print("Bot: Goodbye!")
        break

    if not user_message:
        continue

    try:
        response = client.responses.create(
            model=MODEL,
            instructions=INSTRUCTIONS,
            input=user_message,
        )

        print(f"\nBot: {response.output_text}\n")

    except Exception as error:
        print(f"\nSomething went wrong: {error}\n")
