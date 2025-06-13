import google.generativeai as genai

genai.configure(api_key="AIzaSyCMOSDD0vv34zjFXtf7OW46dMCpwj_17l0")

model = genai.GenerativeModel(model_name="models/gemini-1.5-flash")

print("Welcome to your Mood Companion 🤖✨")
while True:
    mood = input("You (type your mood or 'exit'): ")
    if mood.lower() == "exit":
        print("Bot: Take care, sunshine! ☀️")
        break
    prompt = f"I am feeling {mood}. Suggest something thoughtful or uplifting."
    response = model.generate_content(prompt)
    print("Bot:", response.text)