from groq import Groq
import os
from dotenv import load_dotenv

load_dotenv()

client = Groq(api_key=os.getenv("GROQ_API_KEY"))
conversation = [
    {
        "role": "system",
        "content": "You are a helpful AI tutor. Keep explanations simple."
    }
]
def chat(user_message):
    conversation.append(
        {
            "role": "user",
            "content": user_message
        }
    )

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=conversation
    )

    reply = response.choices[0].message.content

    conversation.append(
        {
            "role": "assistant",
            "content": reply
        }
    )

    return reply

while True:
    user_input = input("\nYou: ")

    if user_input.lower() == "exit":
        break

    reply = chat(user_input)
    print("\nConversation History:")
    print(conversation)
    print("\nAI:", reply)