import time
from clases.voz import SpeechModule, VoiceRecognitionModule 
from clases.ChatBot import ChatBot

speech = SpeechModule()
recognition = VoiceRecognitionModule()

while True:
    text = recognition.recognize()
    
    if "Amy" in text:
        
        mandar="¿Que necesitas papu?"
        print(text,"\n",mandar)
        speech.talk(mandar)
        
        text = recognition.recognize()

        if text:
            ChatBot_resultado = ChatBot.text(text)
            print(text,"\n",ChatBot_resultado)
            speech.talk(ChatBot_resultado)
    time.sleep(1)