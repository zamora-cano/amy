import random, json, urllib.request
from clases.chatGPT import ChatGPTClient 

class ChatBot():
    def __init__(self):
        pass
    
    def text(input):
        conversacion = {
            "hola":["Hola, soy una inteligencia artificial... más o menos","Hola, ¿En qué puedo ayudarte?","Hola, ¿Necesitas algo? podría ayudarte"],
            "cómo estás":["Bien, gracias por preguntar","Robotica... jaja, no cierto estoy bien",""],
            "cuál es tu color favorito":["No tengo un color favorito","Soy un robot, no tengo un color favorito","No tengo un color favorito, pero el azul es cómo relacionan la tecnología."],
            "cuál es tu canción favorita":['"This is what falling in love", me encanta esa canción','¿Yá escuchaste "This is what falling in love"? esa canción me encanta muchisimo','¿Mi canción favorita? siempre será "This is what falling in love"'],
            "cuál es tu canción favorito":['"This is what falling in love", me encanta esa canción','¿Yá escuchaste "This is what falling in love"? esa canción me encanta muchisimo','¿Mi canción favorita? siempre será "This is what falling in love"'],
            }
        
        input = input.lower()
        
        if input in conversacion:
            numero = random.randint(0,2)
            return conversacion[input][numero]
        
        elif "un dado" in input:
            try: 
                tira_un_dado=["El resultado es: ","Ha salido un: ","Tenemos suerte, ha salido un: "]
                tira_un_dado6=["Perfecto, salió un: ","Maravilloso, salió un: ", "Estamos de suerte, tenemos un: "]
                resultado = random.randint(1,6)
                if resultado == 6:
                    resultado = (tira_un_dado6[random.randint(0,2)]+str(resultado))
                else:
                    resultado = (tira_un_dado[random.randint(0,2)]+str(resultado))
            except:
                resultado = "Hubo un problema"
            return resultado
        
        elif "dos dados" in input:
            try: 
                tira_un_dado=["El resultado es: ","Ha salido un: ","Tenemos suerte, ha salido un: "]
                tira_un_dado6=["Perfecto, salió un: ","Maravilloso, salió un: ", "Estamos de suerte, tenemos un: "]
                resultado = random.randint(2,12)
                if resultado >= 10:
                    resultado = (tira_un_dado6[random.randint(0,2)]+str(resultado))
                else:
                    resultado = (tira_un_dado[random.randint(0,2)]+str(resultado))
            except:
                resultado = "Hubo un problema"
            return resultado
        
        elif "más" in input and "cuánto es" in input:
            try:
                resultado = input.replace("cuánto es","").replace("más","")
                resultado = json.load(resultado)
            except:
                resultado = "Hubo un problema en la suma"
            return resultado
        elif "cuántos suscriptores tiene" in input:
            try:
                accion = input.replace("cuántos suscriptores tiene","")
                data = urllib.request.urlopen(f'https://www.googleapis.com/youtube/v3/channels?part=statistics&forUsername={accion}&key=AIzaSyD_Ul6O39PZf5sVbiMsU9gTWMx3Pq-zz2E').read()
                subs = json.loads(data)["items"][0]["statistics"]["subscriberCount"]
                resultado = accion + " tiene {:,d}".format(int(subs)) + " suscriptores!"
            except:
                resultado = "Lo siento, no hay conexion de internet"
            return resultado
        else:
            client = ChatGPTClient()

            response_data = client.generate_response_choices(input)
            return response_data
            return "Nada"
