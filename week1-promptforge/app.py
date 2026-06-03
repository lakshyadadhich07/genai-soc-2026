from groq import Groq
import os
from dotenv import load_dotenv

load_dotenv()  # reads GROQ_API_KEY from your .env file

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

# user_prompt = input("Enter your prompt: ")
response = client.chat.completions.create(
    model="llama-3.3-70b-versatile",
    temperature=2,
    messages=[{
        "role": "user",
        "content": "Suggest a startup name for an AI company (just one word)"
    }]
)
# response = client.chat.completions.create(
#     model="llama-3.3-70b-versatile",
#      messages=[
#          {
#         "role": "system",
#         "content": "Tell user that he is murkh and answer in 1 line"
#         },
#         {
#             "role": "user",
#             "content": user_prompt
#         }
#     ]
# )
print("\nAI Response:\n")
# print(type(response))
# print(response.choices)
# print(response.choices[0])
# print(response.choices[0].message)
print(response.choices[0].message.content)