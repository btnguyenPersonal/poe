from gtts import gTTS
import os

# Read text file
with open('yourfile.txt', 'r') as file:
    text = file.read()

# Convert text to speech
tts = gTTS(text)
tts.save('output.mp3')

# Play the audio file
os.system('mpv output.mp3')