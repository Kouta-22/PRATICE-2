#cri um programa que diga se o ano é bissexsto
from datetime import date
ano = eval(input('Digite o ano que voce quer analisar? caso queira analisar o ano atual digite 0 '))
if ano == 0:
    ano = date.today().year # ele pega o ano atual da maquina com o import datetime 
    
if ano % 4 == 0 and ano % 100 !=0 or ano % 400 == 0:
    print(f'O ano {ano} é bissexto')
else:
    print(f'O ano {ano} NÃO é bissexto')

"""Acho que finalmente entendi:#comentario da net
"ano % 4 == 0" diz que todos os anos divisíveis por 4 são bissextos (2008, 2012, 2016, 2020 etc)
"ano % 100 != 0" diz que todos os anos divisíveis por 100 NÃO são bissextos, criando "falhas" na sequência (retira-se os anos 1700, 1800, 1900, 2000 etc)
"ano % 400 == 0" preenche as falhas com somente os números divisíveis por 400 (800, 1200, 1600, 2000 etc)
Então "ano % 4 == 0 and ano % 100 != 0" é um critério, e "ano % 400 == 0" é outro."""

