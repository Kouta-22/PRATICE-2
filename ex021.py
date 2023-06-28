#Como tocar uma musica mp3 no python
from time import sleep
import pygame
pygame.init()
print('\n\033[1;37;41m Digite 1 para kero kero bonito!!!\033[m')
print('\n\033[1;37;44m Digite 2 para BoyWithUke!!!\033[m')
select = eval(input('\nEscolha: '))

if select == 1:
    print('A musica ira tocar em: ')
    print('1')
    sleep(1)
    print('2')
    sleep(1)
    print('3')
    sleep(1)
    print('\n\033[1;37;41mVoce escolheu kero kero bonito a musica que ira tocar é flamingo\033[m')
    pygame.mixer.music.load("C:/Users/guilh/OneDrive/Área de Trabalho/estudos_py/aulas_00_a_63/ex021.mp3")
    pygame.mixer.music.play()
else:
    receptor = ['A musica ira tocar em: ','1','2','3'] #declaro um variavel para criar as strings
    for cont in receptor: # aqui eu uso o laço for para ler elas
        print(cont) # e aqui para imprimir onde ela foi armazenada "cont"
        sleep(1)
        
    print('\n\033[1;37;44mVoce escolheu BoyWithUke a musica que ira tocar é toxic\033[m')
    pygame.mixer.music.load("C:/Users/guilh/OneDrive/Área de Trabalho/estudos_py/aulas_00_a_63/ex022.mp3")
    pygame.mixer.music.play()

input("\n\n\033[7;30;47mtecle ENTER para finalizar a musica: \033[m")
pygame.event.wait()



"""

"""

#estava dando erro porque não usei a maquina virtual e teve um lance com o json



