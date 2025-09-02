import os
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

MODEL_NAME = "gemini-1.5-flash"

model = genai.GenerativeModel(MODEL_NAME)
chat = model.start_chat(history=[])

print("Gemini Chatbot")
while True:
    user_input = input("You: ")
    if user_input.lower() in ["exit"]:
        print("Bot: Thank You!")
        break
    response = chat.send_message(user_input)
    print("Bot:", response.text.strip())
