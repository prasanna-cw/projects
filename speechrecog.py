import speech_recognition as sr
import datetime

r = sr.Recognizer()
with sr.Microphone() as source:
    print("listening...")
    audio = r.listen(source)

try:
    text = r.recognize_google(audio)
    print("{}".format(text))

except:
    print("sorry we cant recognize the audio")