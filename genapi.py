import google.generativeai as genai

genai.configure(api_key="AIzaSyBYq1OpCeejvnImmc8kRSWNjbg0mheqiio")

model = genai.GenerativeModel("gemini-1.5-flash")

def ask_gemini(question):
    response = model.generate_content(question)
    return response.text
def chat():
    print("Gemini Chatbot\n")
    while True:
        user_input = input("You: ")
        if user_input.lower() in ["exit"]:
            print("Bot: Goodbye! 👋")
            break
        answer = ask_gemini(user_input)
        print("Bot:", answer)

if __name__ == "__main__":
    chat()
