import os
from dotenv import load_dotenv
import google.generativeai as genai

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")
genai.configure(api_key=api_key)

model = genai.GenerativeModel(
    "models/gemini-2.5-flash",
    system_instruction="Always reply in simple text. Do NOT use LaTeX or $ symbols."
)

print("Chatbot started! Type 'exit' to stop")

chat_history = []

while True:
    user_input = input("You: ")

    if user_input.lower() == "exit":
        print("Chat ended.")
        break

    chat_history.append(f"You: {user_input}")
    full_prompt = "\n".join(chat_history)

    try:
        response = model.generate_content(full_prompt)
        chat_history.append(f"AI: {response.text}")
        print("AI:", response.text)

    except Exception as e:
        print("Error:", e)