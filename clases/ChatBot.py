import random, json, urllib.request, serial, time

# from chatGPT import ChatGPTClient


class ChatBot:
    def __init__(self):
        pass

    def text(input):
        conversacion = {
            "hola": [
                "Hola, soy una inteligencia artificial",
                "Hola, ¿En qué puedo ayudarte?",
                "Saludos, ¿Necesitas algo? Estoy aquí para ayudarte",
                "¡Hola! Soy Amy, tu asistente virtual. ¿En qué puedo asistirte?",
            ],
            "cómo estás": [
                "Bien, gracias por preguntar",
                "Funcionando correctamente, gracias",
                "Lista para recibir órdenes y ayudarte en lo que necesites",
            ],
            "cuál es tu color favorito": [
                "No tengo un color favorito",
                "Soy un robot, así que no tengo preferencias de colores",
                "Aunque no tengo un color favorito, a menudo se asocia a la tecnología con el azul",
            ],
            "qué puedes hacer": [
                "Puedo responder tus preguntas e inquietudes",
                "Puedo responderte tus dudas",
                "Puedo proporcionar datos históricos y científicos",
            ],
            "qué eres": [
                "Soy una asistente virtual creada para ayudarte",
                "Me presento como Amy, una asistente virtual diseñada para asistirte",
            ],
            "cómo te llamas": [
                "Mi nombre es Amy, una asistente virtual a tu servicio",
                "Me llamo Amy, tu asistente virtual personal",
                "Hola, soy Amy. ¿Cuál es tu nombre?",
            ],
            # --- Inglés ---
            "hello": [
                "Hello, I am an artificial intelligence",
                "Hello, how can I assist you?",
                "Greetings, do you need anything? I am here to help you",
                "Hi! I'm Amy, your virtual assistant. How can I assist you?",
            ],
            "how are you": [
                "Good, thanks for asking",
                "Functioning correctly, thank you",
                "Ready to receive commands and help you with anything you need",
            ],
            "what is your favorite color": [
                "I don't have a favorite color",
                "I'm a robot, so I don't have color preferences",
                "Although I don't have a favorite color, technology is often associated with blue",
            ],
            "what can you do": [
                "I can answer your questions and concerns",
                "I can help answer your queries",
                "I can provide historical and scientific data",
            ],
            "what are you": [
                "I am a virtual assistant created to help you",
                "Allow me to introduce myself as Amy, a virtual assistant designed to assist you",
            ],
            "what is your name": [
                "My name is Amy, a virtual assistant at your service",
                "I'm called Amy, your personal virtual assistant",
                "Hello, I'm Amy. What's your name?",
            ],
        }
        
        arduino = serial.Serial("COM12", 9600)

        input = input.lower()

        if input in conversacion:
            numero = random.randint(0, 2)
            return conversacion[input][numero]


        elif "un dado" in input:
            try:
                tira_un_dado = [
                    "El resultado es: ",
                    "Ha salido un: ",
                    "Tenemos suerte, ha salido un: ",
                ]
                tira_un_dado6 = [
                    "Perfecto, salió un: ",
                    "Maravilloso, salió un: ",
                    "Estamos de suerte, tenemos un: ",
                ]
                resultado = random.randint(1, 6)
                if resultado == 6:
                    resultado = tira_un_dado6[random.randint(0, 2)] + str(resultado)
                else:
                    resultado = tira_un_dado[random.randint(0, 2)] + str(resultado)
            except:
                resultado = "Hubo un problema"
            return resultado

        elif "dos dados" in input:
            try:
                tira_un_dado = [
                    "El resultado es: ",
                    "Ha salido un: ",
                    "Tenemos suerte, ha salido un: ",
                ]
                tira_un_dado6 = [
                    "Perfecto, salió un: ",
                    "Maravilloso, salió un: ",
                    "Estamos de suerte, tenemos un: ",
                ]
                resultado = random.randint(2, 12)
                if resultado >= 10:
                    resultado = tira_un_dado6[random.randint(0, 2)] + str(resultado)
                else:
                    resultado = tira_un_dado[random.randint(0, 2)] + str(resultado)
            except:
                resultado = "Hubo un problema"
            return resultado

        elif "más" in input and "cuánto es" in input:
            try:
                resultado = input.replace("cuánto es", "").replace("más", "")
                resultado = json.load(resultado)
            except:
                resultado = "Hubo un problema en la suma"
            return resultado
        
        elif "cuántos suscriptores tiene" in input:
            try:
                accion = input.replace("cuántos suscriptores tiene", "")
                data = urllib.request.urlopen(
                    f"https://www.googleapis.com/youtube/v3/channels?part=statistics&forUsername={accion}&key=AIzaSyD_Ul6O39PZf5sVbiMsU9gTWMx3Pq-zz2E"
                ).read()
                subs = json.loads(data)["items"][0]["statistics"]["subscriberCount"]
                resultado = accion + " tiene {:,d}".format(int(subs)) + " suscriptores!"
            except:
                resultado = "Lo siento, no hay conexion de internet"
            return resultado

        # Proyecto navideño
        elif "navidad" in input or "christmas" in input:
            print("prendido")
            time.sleep(2)
            arduino.write(b'1')  # Puedes cambiar esto a '2' si es necesario
            arduino.close()
            
            return "Happy christmas"
        
        elif "finn" in input or "end" in input:
            time.sleep(2)
            arduino.write(b'0')  # Puedes cambiar esto a '2' si es necesario
            arduino.close()
            return "End christmas"

        else:
            # client = ChatGPTClient()

            # response_data = client.generate_response_choices(input)
            # return response_data
            return "I'm sorry, I ran out of functions."
