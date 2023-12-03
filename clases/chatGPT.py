"""
    ChatGPT
    https://rapidapi.com/Glavier/api/chatgpt53
"""

import requests


class ChatGPTClient:
    def __init__(
        self,
        base_url="https://chatgpt53.p.rapidapi.com/",
        api_key="7fedda9116msh32fa6fe00faafa6p1b499djsn46077a884ed9",
    ):
        self.api_key = api_key
        self.base_url = base_url
        self.headers = {
            "content-type": "application/json",
            "X-RapidAPI-Key": self.api_key,
            "X-RapidAPI-Host": "chatgpt53.p.rapidapi.com",
        }

    def generate_response(self, user_message, temperature=1):
        payload = {
            "messages": [{"role": "user", "content": user_message}],
            "temperature": temperature,
        }

        response = requests.post(self.base_url, json=payload, headers=self.headers)
        return response.json()

    def generate_response_OnlyText(self, user_message, temperature=1):
        payload = {
            "messages": [{"role": "user", "content": user_message}],
            "temperature": temperature,
        }

        response = requests.post(self.base_url, json=payload, headers=self.headers)
        try:
            response_data = response.json()["choices"][0]["message"]["content"]
            return response_data
        except KeyError as e:
            print(f"Error: {e}")
            print(response.json())  # Imprime la respuesta completa para depuración
            return "Respuesta inesperada"
    



client = ChatGPTClient()

texto = "can you tell me what is a developer"
response_data = client.generate_response_OnlyText(texto)

print(response_data)
