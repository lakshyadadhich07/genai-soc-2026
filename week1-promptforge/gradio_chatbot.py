import gradio as gr
from groq import Groq
import os
from dotenv import load_dotenv

load_dotenv()

client = Groq(api_key=os.getenv("GROQ_API_KEY"))
def chat(message, history):

    messages = [
        {
            "role": "system",
            "content": "You are a helpful AI tutor."
        }
    ]

    for item in history:

        role = item["role"]

        content = item["content"][0]["text"]

        messages.append(
            {
                "role": role,
                "content": content
            }
        )

    messages.append(
        {
            "role": "user",
            "content": message
        }
    )

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=messages
    )

    return response.choices[0].message.content

gr.ChatInterface(
    fn=chat,
    title="My First AI Chatbot"
).launch()