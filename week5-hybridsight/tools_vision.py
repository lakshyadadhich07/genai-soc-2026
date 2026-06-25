import os

from dotenv import (
    load_dotenv
)

from langchain_groq import (
    ChatGroq
)

from langchain_core.tools import (
    tool
)

from image_utils import (
    encode_image
)

load_dotenv()


vision = ChatGroq(
    model="meta-llama/llama-4-scout-17b-16e-instruct",
    api_key=os.getenv("GROQ_API_KEY"),
    temperature=0
)


@tool
def describe_image(
    image_path: str
):

    """
    Describe uploaded image.
    """

    image = encode_image(
        image_path
    )

    response = (

        vision.invoke(

            [

                {

                    "role":
                    "user",

                    "content": [

                        {

                            "type":
                            "text",

                            "text":
                            "Describe this image."

                        },

                        {

                            "type":
                            "image_url",

                            "image_url": {

                                "url":

                                f"data:image/jpeg;base64,{image}"

                            }

                        }

                    ]

                }

            ]

        )

    )

    return response.content