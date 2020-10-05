"""
gTTS (Google Text-to-Speech), a Python library and CLI tool to interface with Google Translate's text-to-speech API. Write spoken mp3 data to a file, a file-like object (bytestring) for further audio manipulation, or stdout.

https://pypi.org/project/gTTS/
"""

# import os
from gtts import gTTS

from playsound import playsound

# all available languages along with their IETF tags
# print(gtts.lang.tts_langs())

lang = "ru"

with open("text.txt", "r") as text_to_speech:

    text_to_speech = text_to_speech.read().replace("\n", " ")

    output = gTTS(text=text_to_speech, lang=lang, slow=False)

    output.save("my_file.mp3")


# os.system("start my_file.mp3") to play with default system player

playsound("my_file.mp3")
