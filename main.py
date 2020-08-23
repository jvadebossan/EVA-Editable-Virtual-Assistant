from configs import *
import speech_recognition as sr
from random import choice
import pyttsx3
import datetime
import sys
from time import sleep as wait
import webbrowser


def intro():
    print('=============================================================================================')
    print('=  version: ' + version, '                   ' + name, 'assistant' '                  made by' + creator, '  =')
    print('=============================================================================================')
    frase_intro = ('{} assistente, versão {} feito por {}'.format(name_to_talk, version, creator_to_talk) )
    say(frase_intro)
    start()

def restart():
    wait(0.2)
    start()

def reboot():
    wait(0.2)
    intro()

def say(tosay):
    engine = pyttsx3.init()
    engine.say(tosay)
    engine.runAndWait()

def start():
    while True:
        r = sr.Recognizer()
        with sr.Microphone() as fonte:
            print('ouvindo...')
            audio = r.listen(fonte)
            textc = r.recognize_google(audio, language='pt-br')            
            text = textc.lower()
            print(text)
            try:
                #função boas vindas
                if text == str(name):
                    msg_boas_vindas = choice(l_boas_vindas)
                    say(msg_boas_vindas)
                
                #função tocar música
                elif text == str('tocar minha playlist'):
                    webbrowser.open(playlist, new=2)
                
                #função dia
                elif text == str('que dia é hoje'):
                    print(dia)
                    say(dia)

                #função horas
                elif text == str('que horas são'):
                        print(hr)
                        say(hr)

			    #função piadas
                elif text == str('piada'):
                    joke = (choice(l_piadas))
                    joke = choice(l_piadas)
                    print (joke)
                    say(joke)

                #função desligar
                elif text == str('desligar sistema'):
                    desligando = str('desligando em 3, 2, 1')
                    print (desligando)
                    sys.exit()

                #função reiniciar
                elif text == str('reiniciar sistema'):
                    reiniciando = str('reiniciando em 3, 2, 1')
                    print (reiniciando)
                    reboot()
				    

            except:
                restart()
intro()