
import os 
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()  

client = OpenAI(
      api_key=os.environ.get("OPENAI_API_KEY"),
)

messages = []
system_msg = input("What type of chatbot would you like to create?\n")
messages.append({"role": "system", "content": system_msg})

print("Your new assistant is ready!")
while input != "quit()":
    message = input()
    messages.append({"role": "user", "content": message})
    chat_completion = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=messages)
    reply = chat_completion.choices[0].message.content
    messages.append({"role": "assistant", "content": reply})
    print("\n" + reply + "\n")