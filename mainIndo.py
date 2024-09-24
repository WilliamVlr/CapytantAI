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
                # print("Maaf, saya tidak bisa memahami apa yang kamu katakan.")
                # speak("Maaf tuan, saya tidak bisa memahami apa yang kamu katakan.")
                restPlay()
                return('...')
            except sr.RequestError as e:
                print(f"Tidak dapat meminta hasil dari Google Speech Recognition service; {e}")
                speak("Maaf tuan, servis sedang tidak dapat dihubungi")
                return('...')
    except:
        # speak('Tuan, kapiten akan istirahat')
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

def current_weather():
    try:
        speak('Tuan sedang berada di kota mana?')
        city_name = listen()
        # city_name = 'Bogor'
        API_KEY = '3ab9623ddd6d07b1498404abc16767f3'
        url_weather = f'https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={API_KEY}&units=metric'

        response = requests.get(url_weather)
    
        if response.status_code == 200:
            data = response.json()
            cuaca = data['weather'][0]['description']
            # print("The weather today is", cuaca)
            cuacatxt = translator.translate(cuaca, src='auto', dest='id').text
            speak('Cuaca '+city_name+' hari ini adalah '+cuacatxt)
    except: 
        print(f'Tidak bisa memprediksi cuaca saat ini')

def get_news(country='bitcoin', api_key='0cbe470ef3c04e8a8933170cd457aa43'):
    url = f'https://newsapi.org/v2/everything?q={country}&apiKey={api_key}'
    r = requests.get(url)
    content = r.json()
    articles = content['articles']
    # print(articles)
    if not articles:
        choosen_article = random.choice(articles)
        print(choosen_article['title'])
        return 'Berita terbaru saat ini' + choosen_article['title']
    else:
        return 'Tidak ada berita terbaru'

def v_command():
    command = listen()
    if command != '...':
        time.sleep(1)
        if 'kapiten' in command or 'halo' in command:
            speak('iya tuan')
            return '...'
        elif 'nyalakan' in command or 'Nyalakan' in command or 'hidupkan' in command or 'nyala' in command:
            if 'kamar' in command:
                speak('Menyalakan lampu kamar')
                return 'nk'
            elif 'balkon' in command:
                speak("Menyalakan lampu balkon")
                return 'nb'
            elif 'dapur' in command:
                speak("Menyalakan lampu dapur")
                return 'nd'
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
            elif 'balkon' in command:
                speak('Mematikan lampu balkon')
                return 'mb'
            elif 'dapur' in command:
                speak('Mematikan lampu dapur')
                return 'md'
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
        elif 'cuaca' in command:
            current_weather()
            return '...'
        elif 'berita' in command or 'terbaru' in command:
            news = f'{get_news()}'
            speak(news)
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