import datetime

#padrão ==============================================
version = ('0.1')
creator = str('@jvadebossan')
creator_to_talk = str('@ j v a debossan')

#variaveis de dia e hora
dia1 = datetime.datetime.now()
dia = ('hoje é dia {} do {} de {}'.format(dia1.day, dia1.month, dia1.year))

hr1 = datetime.datetime.now()
hr = hr1.strftime("%H:%M")


#editaveis ========================================
name_to_talk = ('éva') #fonética
name = ('eva') #nome correto

playlist = ('https://open.spotify.com/')
user_name = ('joão vitor')

#listas
l_boas_vindas = [
'o que você precisa, {}'.format(user_name),
'seja bem vindo de volta,{}'.format(user_name),
'olá {}'.format(user_name),
'sim'
'pode falar'
]

l_piadas = [
'o que é um pontinho vermelho no castelo, , ,  é uma pimenta do reino ',
'o que é um pontinho amarelo na africa, , ,  é um ieloufante',
'porque a plantinha nao foi atendida no hospital, , ,  porque só tinha médico de plantão',
'o que o pagodeiro foi fazer na igreja, , ,  ele foi cantar pa god',
'o que acontece quando chove na inglaterra, , ,  ela vira inglalama',
]
