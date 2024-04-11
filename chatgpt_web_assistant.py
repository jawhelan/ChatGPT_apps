
import os 
from dotenv import load_dotenv
from openai import OpenAI
import gradio


load_dotenv()  

client = OpenAI(
       api_key=os.environ.get("OPENAI_API_KEY"),
)

messages = [{"role": "system", "content": "You are a python programming expert"}]

def CustomChatGPT(user_input):
    messages.append({"role": "user", "content": user_input})
    chat_completion = client.chat.completions.create(
        model = "gpt-3.5-turbo",
        messages = messages
    )
    ChatGPT_reply = chat_completion.choices[0].message.content
    messages.append({"role": "assistant", "content": ChatGPT_reply})
    return ChatGPT_reply

demo = gradio.Interface(fn=CustomChatGPT, inputs = "text", outputs = "text", title = "Python Pro")

demo.launch(share=True)