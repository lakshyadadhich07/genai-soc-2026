from groq import Groq
import os
from dotenv import load_dotenv

load_dotenv()  # reads GROQ_API_KEY from your .env file

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

user_prompt = input("Enter your prompt: ")
response = client.chat.completions.create(
    model="llama-3.3-70b-versatile",
     messages=[
         {
        "role": "system",
        "content": "You are a joker and explain in most humorous way and answer in 1 line"
        },
        {
            "role": "user",
            "content": user_prompt
        }
    ]
)
print("\nAI Response:\n")
# print(type(response))
# print(response.choices)
# print(response.choices[0])
# print(response.choices[0].message)
print(response.choices[0].message.content)