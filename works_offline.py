"""
pyttsx3 is a text-to-speech conversion library in Python. Works without internet connection or delay.

https://pypi.org/project/pyttsx3/

pyttsx3 library looks for TTS engines pre-installed in your platform, here are the text-to-speech synthesizers that this library uses:


Microsoft Speech API (SAPI5) on Windows

List of available languages: https://support.microsoft.com/en-us/help/22805/windows-10-supported-narrator-languages-voices

How to install new languages: https://support.microsoft.com/en-us/office/how-to-download-text-to-speech-languages-for-windows-10-d5a6b612-b3ae-423f-afa5-4f6caf1ec5d3


espeak on Ubuntu
make sure that 'espeak', 'ffmpeg', 'libespeak1' are installed
sudo apt update && sudo apt install espeak ffmpeg libespeak1


NSSpeechSynthesizer on macOS
"""

import pyttsx3

engine = pyttsx3.init()

# get speaking rates
rate = engine.getProperty("rate")
engine.setProperty("rate", 200)  # 200 is default rate


# get all voices available
voices = engine.getProperty("voices")
# for voice in voices:
#     print("ID:", voice.id)
engine.setProperty(
    "voice", "english"
)  # for linux system; linux includes only male voices

# for windows 10
# voice_id = "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_RU-RU_IRINA_11.0"
# engine.setProperty("voice", voice_id)

# change volume
volume = engine.getProperty("volume")
engine.setProperty("volume", 1.0)  # setting up volume level  between 0.0 and 1.0


with open("text.txt", "r", encoding="utf-8") as text:
    text = text.read().replace("\n", " ")

    # Saving to a file
    engine.save_to_file(text, "offline.mp3")
    engine.runAndWait()


"""
runAndWait()
    Blocks while processing all currently queued commands. Invokes callbacks for engine notifications appropriately. Returns when all commands queued before this call are emptied from the queue.
"""
