import os 
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()  

client = OpenAI(
    # This is the default and can be omitted
    api_key=os.environ.get("OPENAI_API_KEY"),
)
    
question= input("Enter your question:\n")

chat_completion = client.chat.completions.create(
   
     model="gpt-3.5-turbo",
     messages=[
          {"role": "system", "content": "You are a helpful assistant."},
          {"role": "user", "content": question},
          ]
    )

print(chat_completion.choices[0].message.content)