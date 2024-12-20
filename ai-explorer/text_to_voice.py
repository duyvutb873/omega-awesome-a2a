import pyttsx3

engine = pyttsx3.init() 

rate = engine.getProperty('rate')
engine.setProperty('rate', rate-50) 

voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

text = "Hello, I am a text to speech engine. I can convert text to speech."
engine.say(text)

engine.runAndWait()