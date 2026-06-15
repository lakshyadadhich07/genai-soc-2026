from langchain_core.tools import tool

@tool
def play_music(song: str):
    """
    Play a song by name.
    """
    return f"🎵 Now playing: {song}"

print(play_music.name)
print(play_music.description)
print(play_music.args)

print()

result = play_music.invoke({
    "song": "Believer"
})

print(result)