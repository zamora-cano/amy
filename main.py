import time
from clases.voz import SpeechModule, VoiceRecognitionModule 
from clases.ChatBot import ChatBot

speech = SpeechModule()
recognition = VoiceRecognitionModule()
chatbot_instance = ChatBot()

while True:
    text = recognition.recognize()
    
    if "Amy" in text:
        mandar = "¿Que necesitas papu?"
        print(text, "\n", mandar)
        speech.talk(mandar)
        
        text = recognition.recognize()

        if text:
            # Usar la instancia de ChatBot creada previamente
            ChatBot_resultado = chatbot_instance.text(input_text=text)
            print(text, "\n", ChatBot_resultado)
            speech.talk(ChatBot_resultado)

    time.sleep(1)