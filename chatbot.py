import os
from dotenv import load_dotenv
import google.generativeai as genai

load_dotenv()

api_key=os.getenv("GEMINI_API_KEY")

genai.configure(api_key=api_key)

model = genai.GenerativeModel("models/gemini-2.5-flash")

print("Chatbot started! Type 'exit' to stop")
chat_history=[]

while True:
    user_input = input("You: ")

    if user_input.lower() == "exit":
        print("Chat ended.")
        break
    chat_history.append(f"you:{user_input}")
    full_prompt="\n".join(chat_history)

    response = model.generate_content(user_input)
    try:
        response=model.generate_content(full_prompt)
        chat_history.append(f"AI:{response.text}")
        print("AI:", response.text)
    except Exception as e:
        print("Error:", e)