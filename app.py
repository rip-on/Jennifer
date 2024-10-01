import pyttsx3 as rip

engine = rip.init()
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)
engine.say("Hi there, I'm your virtual assistant")
engine.runAndWait()