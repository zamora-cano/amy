from clases.voz import SpeechModule

if __name__ == "__main__":
    speech_module = SpeechModule()

    # Obtener información sobre las voces disponibles
    print("\n\n----- Voces -----\n")
    speech_module.get_available_voices()