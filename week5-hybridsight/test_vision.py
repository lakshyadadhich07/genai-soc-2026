from tools_vision import describe_image

print(
    describe_image.invoke(
        {
            "image_path":
            r"C:\Users\camah\Web development\genai-soc-2026\image.png"
        }
    )
)