import speech_recognition as sr
from gtts import gTTS
import os
import requests
import wolframalpha
from playsound import playsound
import pygame
import time
from simple_sender import simple_sender
from googletrans import Translator
import random

r = sr.Recognizer()
translator = Translator()
remote = simple_sender()
run = True
first = False
rest = True

def speak(text):
    speech = gTTS(text=text, lang='id', slow=False, tld='com')
    
    # Save the audio file to a temporary file
    speech_file = 'speech.mp3'
    speech.save(speech_file)
    
    # Initialize pygame mixer
    pygame.mixer.init()
    
    # Load and play the audio file
    pygame.mixer.music.load(speech_file)
    pygame.mixer.music.play()
    
    # Wait until playback is finished
    while pygame.mixer.music.get_busy():
        continue
    
    # Clean up
    pygame.mixer.music.unload()
    os.remove(speech_file)

def firstPlay():
    speak('kapiten siap membantu')

def restPlay():
    speak('Tuan, kapiten akan beristirahat')


def listen():
    url = "http://google.com"
    timeout = 5
    try:
        request = requests.get(url, timeout=timeout)
        with sr.Microphone() as source:
            # speak('Halo tuan')
            print('Silakan berbicara...')
            r.adjust_for_ambient_noise(source)
            audio = r.listen(source)

            try:
                text = r.recognize_google(audio, language='id-ID')
                print(f"Tuan mengatakan: {text}")
                return text
            except sr.UnknownValueError:
                return('...')
            except sr.RequestError as e:
                print(f"Tidak dapat meminta hasil dari Google Speech Recognition service; {e}")
                speak("Maaf tuan, servis sedang tidak dapat dihubungi")
                return('...')
    except:
        return('...')

def wolframAlpha(text):
    try:
        app_id = "5739R2-9PHHUGQR52"
        client = wolframalpha.Client(app_id)
        res = client.query(text)
        answer = next(res.results).text
        speak(answer)
        # complete = text + '=' + answer
        # speak(complete)
    except:
        try:
            url = "https://google.com"
            timeout = 5
            request = requests.get(url, timeout=timeout)
            speak('Maaf tuan, tapi saya belum bisa menjawabnya')
        except:
            speak('Maaf tuan, tidak ada koneksi internet')

def v_command():
    command = listen()
    if command != '...':
        time.sleep(1)
        if 'nyalakan' in command or 'Nyalakan' in command or 'hidupkan' in command or 'nyala' in command:
            if 'malam' in command:
                speak('Menyalakan lampu malam')
                return 'nk'
            elif 'proyektor' in command:
                speak("Menyalakan proyektor")
                return 'np'
            elif 'kipas' in command:
                speak("Menyalakan kipas angin")
                return 'ns'
        elif 'Matikan' in command or 'matikan' in command:
            if 'kamar' in command:
                speak('Mematikan lampu kamar')
                return 'mk'
            elif 'proyektor' in command:
                speak('Mematikan proyektor')
                return 'mp'
            elif 'kipas' in command:
                speak("Mematikan kipas angin")
                return 'ms'
        elif 'hitung' in command:
            speak('Sebutkan perhitungan yang diinginkan')
            quest = listen()
            wolframAlpha(quest)
            return '...'
        elif 'kapiten' in command or 'halo' in command:
            speak('iya tuan')
            return '...'
        elif 'selesai' in command or 'tutup' in command or 'hentikan' in command:
            speak('menutup layanan kapiten')
            return 'e'
        else:
            speak('Coba ulangi, Tuan')
            return '...'
    else:
        return '...'

while run:
    if first == False:
        first = True
        firstPlay()
        rest = False
    
    command = v_command()
    print(f'command: {command}')
    if command == 'v###' or command == 'e':
        run = False
        break

    if command != '...':
        res = remote.simple_run(command)
        if res == '###':
            run = False
        elif res != None:
            print(res)