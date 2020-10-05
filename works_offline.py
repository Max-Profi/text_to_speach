"""
pyttsx3 is a text-to-speech conversion library in Python. Works without internet connection or delay. Compatible with both Python 2 and 3.

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
print("rate:", rate)

# get all voices available
voices = engine.getProperty("voices")

num = 1
for i in range(1, len(voices)):
    print("voice:", voices[i].id, num)
    num += 1

engine.setProperty("rate", 200)  # 200 is default rate
engine.setProperty("voice", voices[11].id)

text = "Python is a great programming language"

engine.say(text)

engine.runAndWait()


"""
say() method adds an utterance to speak to the event queue, while runAndWait() method runs the actual event loop until all commands queued up. So you can call multiple times the say() method and run a single runAndWait() method in the end, in order to hear the synthesis.
"""
