from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
import os

load_dotenv()

def main():
    model = ChatGoogleGenerativeAI(
        model="gemini-1.5-flash",
        google_api_key=os.getenv("GOOGLE_API_KEY")
    )

    result = model.invoke("What is the capital of France?")
    print(result.content)

if __name__ == "__main__":
    main()