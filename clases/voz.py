import pyttsx3
import speech_recognition as sr


class SpeechModule:
    def __init__(self, voice=1, volume=1, rate=200):
        self.engine = pyttsx3.init()
        self.engine.setProperty("rate", rate)
        self.engine.setProperty("volume", volume)

        voices = self.engine.getProperty("voices")
        self.engine.setProperty("voice", voices[voice].id)

    def get_available_voices(self):
        voices = self.engine.getProperty("voices")
        for i, voice in enumerate(voices):
            print(f"Voice {i}:")
            print(f" - ID: {voice.id}")
            print(f" - Name: {voice.name}")
            print(f" - Languages: {voice.languages}")
            print(f" - Gender: {voice.gender}")
            print()

    def talk(self, text):
        self.engine.say(text)
        self.engine.runAndWait()


class VoiceRecognitionModule:
    def __init__(self, key=None):
        self.key = key
        self.r = sr.Recognizer()

    def recognize(self):
        with sr.Microphone() as source:
            print("Speak Anything : ")
            audio = self.r.listen(source)
            try:
                text = self.r.recognize_google(audio, language="en")
                return text
            except:
                return None
