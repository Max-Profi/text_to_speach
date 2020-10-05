"""
gTTS (Google Text-to-Speech), a Python library and CLI tool to interface with Google Translate's text-to-speech API. Write spoken mp3 data to a file, a file-like object (bytestring) for further audio manipulation, or stdout.

https://pypi.org/project/gTTS/
"""

import os
from gtts import gTTS

# all available languages along with their IETF tags
# print(gtts.lang.tts_langs())

lang = "ru"

with open("text.txt", "r") as text_to_speech:

    text_to_speech = text_to_speech.read().replace("\n", " ")

    output = gTTS(text=text_to_speech, lang=lang, slow=False)

    output.save("online.mp3")


os.system("start online.mp3")  # to play with default system player
