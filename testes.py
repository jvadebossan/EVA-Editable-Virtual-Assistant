import webbrowser
a = input('say something: ')

if ('open') in a:
    if ('google') in a:
        webbrowser.open('www.google.com.br', new=2)
    elif ('youtube') in a:
        webbrowser.open('www.youtube.com', new=2)
    elif ('kahoot') in a:
        webbrowser.open('kahoot.it', new=2)
    else:
        print('aplicativo não encontrado')

elif ('pesquisar') in a:
    print(a)
    webbrowser.open('https://www.google.com/search?q={}&oq={}&aqs=chrome.0.0j46j0l6.1656j1j15&sourceid=chrome&ie=UTF-8'.format(a, a), new=2)

else: 
    print('comando ainda não suportado')
