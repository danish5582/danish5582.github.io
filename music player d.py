import os
import random
import pyttsx3
engine=pyttsx3.init("sapi5")
rate=engine.getProperty("rate")
engine.setProperty('rate',200)
voices=engine.getProperty("voices")
engine.setProperty("voice",voices[0].id)
def speak(s):
    engine.say(s)
    engine.runAndWait()
music_dir = 'D://my music'
songs = os.listdir(music_dir)
d=random.choice(songs)
os.startfile(os.path.join(music_dir,d))