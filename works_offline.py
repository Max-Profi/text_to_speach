"""
pyttsx3 is a text-to-speech conversion library in Python. Works without internet connection or delay.

https://pypi.org/project/pyttsx3/

pyttsx3 library looks for TTS engines pre-installed in your platform, here are the text-to-speech synthesizers that this library uses:

Microsoft Speech API (SAPI5) on Windows
NSSpeechSynthesizer on macOS
espeak on Ubuntu (install via Synaptic)
"""

import pyttsx3

engine = pyttsx3.init()

# get speaking rates
rate = engine.getProperty("rate")
# print("rate:", rate)
engine.setProperty("rate", 200)  # 200 is default rate


# get all voices available
voices = engine.getProperty("voices")
# for voice in voices:
#     print("ID:", voice.id)
#     print("Gender:", voice.gender)
engine.setProperty("voice", "english")
engine.setProperty("voice", "female")  # linux includes only male voices

# engine.setProperty('voice', voices[0].id)  # changes voices. o for male
# engine.setProperty('voice', voices[1].id)  # 1 for female

# change volume
volume = engine.getProperty("volume")
engine.setProperty("volume", 1.0)  # setting up volume level  between 0 and 1


with open("text.txt") as text:
    text = text.read().replace("\n", " ")

    # Saving to a file
    # On linux make sure that 'espeak', 'ffmpeg', 'libespeak1' are installed
    # sudo apt update && sudo apt install espeak ffmpeg libespeak1
    engine.save_to_file(text, "offline.mp3")
    engine.runAndWait()
