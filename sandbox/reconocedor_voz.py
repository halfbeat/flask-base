import speech_recognition as sr

sr.__version__
r = sr.Recognizer()

harvard = sr.AudioFile('harvard.wav')

with harvard as source:
    audio = r.record(source)

type(audio)

r.recognize_google(audio)

import pyttsx3
engine = pyttsx3.init()
engine.setProperty('rate', 110)
engine.say("Me tengo que ir a casa de los abuelos")
engine.runAndWait()

engine.save_to_file('Me tengo que ir a casa de los abuelos', 'test.mp3')
engine.runAndWait()

voices = engine.getProperty('voices')       #getting details of current voice
#engine.setProperty('voice', voices[0].id)  #changing index, changes voices. o for male
engine.setProperty('voice', voices[3].id)   #changing index, changes voices. 1 for female