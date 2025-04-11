import speech_recognition as sr
import os
import datetime
import playsound
import pyjokes
import wikipedia
import pyaudio
import webbrowser

def speak(text):
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Ouvindo...")
        audio = r.listen(source)
        try:
            command = r.recognize_google(audio, language="pt-BR")
            print(f"Voce disse: {command}")
            return command.lower()
        except sr.UnknownValueError:
            print("Desculpe, nao consegui entender o que voce disse.")
            return None
        
def execute_command(command):
    if "horas" in command:
        current_time = datetime.datetime.now().strftime("%H:%M")
        print(f"Agora sao {current_time}.")
        speak(f"Agora sao {current_time}.")
    elif "piada" in command:
        joke = pyjokes.get_joke()
        print(joke)
        speak(joke)
    elif "wikipédia" in command:
        search_query = command.replace("wikipedia", "").strip()
        result = wikipedia.summary(search_query, sentences=1)
        print(result)
        speak(result)
    elif "abrir navegador" in command:
        webbrowser.open("https://www.google.com")
        print("Abrindo navegador...")
    else:
        print("Comando nao reconhecido.")
        speak("Desculpe, nao entendi o comando.")

def main():
    print("Iniciando o assistente de voz...")
    while True:
        command = speak("O que voce gostaria de fazer?")
        if command:
            execute_command(command)
        else:
            print("Tentando novamente...")
        if "sair" in command:
            print("Saindo do assistente de voz.")
            break

if __name__ == "__main__":
    main()