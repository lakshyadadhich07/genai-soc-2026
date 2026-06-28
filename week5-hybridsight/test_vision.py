from tools_vision import describe_image


path = input(
    "Image path: "
)

print()

result = describe_image(
    path
)

print(result)