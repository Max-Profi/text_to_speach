"""
gTTS (Google Text-to-Speech) Python library and CLI tool to interface with Google Translate's text-to-speech API. It can write spoken mp3 data to a file, a file-like object (bytestring) for further audio manipulation.

https://pypi.org/project/gTTS/

On Windows you have to run VS Code as administrator. And it takes a long time to create mp3 file.
"""

# import os
# import gtts
from gtts import gTTS

# # display all available languages along with their IETF tags
# print(gtts.lang.tts_langs(tld="com"))

lang = "en"

with open("text.txt", "r", encoding="utf-8") as text_to_speech:

    text_to_speech = text_to_speech.read().replace("\n", " ")

    output = gTTS(text=text_to_speech, lang=lang, slow=False, lang_check=False)

    output.save("online.mp3")


# os.system("start online.mp3")  # to play with default system player on windows


# # for linux is recommended to use subprocess library
# import subprocess
# subprocess.call("smplayer online.mp3", shell=True)
