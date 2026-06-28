import speech_recognition as sr

recognizer = sr.Recognizer()

with sr.AudioFile("count.wav") as source:
    audio = recognizer.record(source)

text = recognizer.recognize_google(audio)

print(text)


# import speech_recognition as sr

# recognizer = sr.Recognizer()

# with sr.Microphone() as source:
#     print("Speak now...")
#     audio = recognizer.listen(source)

# try:
#     text = recognizer.recognize_google(audio)
#     print("You said:", text)
# except Exception as e:
#     print("Error:", e)