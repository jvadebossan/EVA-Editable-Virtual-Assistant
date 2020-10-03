from configs import *
import speech_recognition as sr
from random import choice
import pyttsx3
import datetime
import sys
from time import sleep as wait
import webbrowser as wb

def intro():
    print('=============================================================================================')
    print('=  version: ' + version, '                   ' + name, 'assistant' '                  made by' + creator, '  =')
    print('=============================================================================================')
    frase_intro = ('{} assistente, versão {} feito por {}'.format(name_to_talk, version, creator_to_talk) )
    say(frase_intro)
    start()

def restart():
    print('.')
    wait(0.2)
    start()

def desligar():
    sys.exit()

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
                engine = pyttsx3.init()
                #função boas vindas
                if text == str(name): #esse ouve o próprio nome dela e responde com um bom dia ou algo do tipo
                    msg_boas_vindas = choice(l_boas_vindas)
                    say(msg_boas_vindas)
                
                #função tocar música
                elif 'playlist' in text:#abre a playlist de muscia do usuário, pre definida em "configs"
                    wb.open(playlist, new=2)
                
                #função dia
                elif 'dia' in text: #fala o dia
                    print(dia)
                    say(dia)

                #função horas
                elif 'horas' in text: #fala as horas
                        print(hr)
                        say(hr)

			    #função piadas
                elif 'piada' in text: # lança a braba
                    joke = (choice(l_piadas))
                    joke = choice(l_piadas)
                    print (joke)
                    say(joke)

                #função desligar
                elif 'desligar' in text: #desliga o sistema
                    desligando = str('desligando em 3, 2, 1')
                    print (desligando)
                    engine.say(desligando)
                    engine.runAndWait()
                    desligar()

                #função reiniciar
                elif 'reiniciar' in text: #reinicia o sistema
                    reiniciando = str('reiniciando em 3, 2, 1')
                    print (reiniciando)
                    engine.say(reiniciando)
                    engine.runAndWait()
                    reboot()

                elif 'fale' in text:
                    texto_falar = text.replace('fale', '')
                    say(texto_falar)

                elif 'pesquis' in text:
                    site_pesquisar = text.replace('pesquis', '')
                    say('pesquisando ' + site_pesquisar)
                    wb.open('https://www.google.com/search?client=opera-gx&hs=5GZ&sxsrf=ALeKk02LWQxX_lhfnlTF6lCi_LYm0x5kqg%3A1601686367378&ei=X8t3X_LeFpPA5OUP0e6-WA&q={}&oq={}&gs_lcp=CgZwc3ktYWIQAzIHCAAQChDLATIECAAQHjoHCCMQ6gIQJzoECCMQJzoFCAAQsQM6CAguELEDEIMBOgIIADoFCC4QsQM6BAgAEAo6BggAEAoQHlD_EVjVH2COImgBcAB4AIABsgKIAdMJkgEHMC41LjAuMZgBAKABAaoBB2d3cy13aXqwAQrAAQE&sclient=psy-ab&ved=0ahUKEwiyiuDXmpfsAhUTILkGHVG3DwsQ4dUDCAw&uact=5'.format(site_pesquisar, site_pesquisar), new=2)
                
                elif text not in comandos:
                    restart()
            except:
                restart()
intro()
