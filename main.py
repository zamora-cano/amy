import time
from clases.voz import SpeechModule, VoiceRecognitionModule 
from clases.action import ChatBot

speech = SpeechModule()
recognition = VoiceRecognitionModule()

while True:
    text = recognition.recognize()
    
    print(text)
    if text:
        ChatBot_resultado = ChatBot.text(text)
        print(text,"\n",ChatBot_resultado)
        speech.talk(ChatBot_resultado)
    time.sleep(1)