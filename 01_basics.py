import pyttsx3
print("hello world")

engine = pyttsx3.init()
engine.say("hello world")
# engine.say("hello world 2")

engine.runAndWait()

engine.say("hello world 2")

engine.runAndWait()