from dotenv import load_dotenv
import os
import base64

from langchain_groq import ChatGroq


load_dotenv()


vision = ChatGroq(
    model="meta-llama/llama-4-scout-17b-16e-instruct",
    api_key=os.getenv("GROQ_API_KEY")
)


def describe_image(image_path):

    try:

        with open(image_path, "rb") as f:
            encoded = base64.b64encode(
                f.read()
            ).decode()

        response = vision.invoke(

            [

                {

                    "role": "user",

                    "content": [

                        {
                            "type": "text",
                            "text": "Describe this image."
                        },

                        {
                            "type": "image_url",

                            "image_url": {

                                "url":

                                f"data:image/png;base64,{encoded}"

                            }

                        }

                    ]

                }

            ]

        )

        return response.content


    except Exception as e:

        return f"Vision Error: {e}"