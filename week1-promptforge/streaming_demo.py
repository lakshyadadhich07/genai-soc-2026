from groq import Groq
import os
from dotenv import load_dotenv

load_dotenv()

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

stream = client.chat.completions.create(
    model="llama-3.3-70b-versatile",
    messages=[
        {
            "role": "user",
            "content": "Write a 1000-word story about a robot learning Python."
        }
    ],
    stream=True #if removed then will wait for full 1000 word to generate then print
)

for chunk in stream:
    print(chunk.choices[0].delta.content or "", end="")