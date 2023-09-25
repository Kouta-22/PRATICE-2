from ssl import ALERT_DESCRIPTION_UNKNOWN_PSK_IDENTITY


sexo = ''
while 'M' != sexo != 'F':
    sexo = str(input('Digite seu sexo [M]asculino [F]eminino: ')).upper()
    if sexo == 'M' or sexo =='F':
        print(f'Sexo {sexo} Registrado!!')
    else:
        print('Sexo invalido')
#versao guanabara
sexo = str(input('Digite seu sexo: ')).upper()
while sexo not in 'MF':
    sexo = str(input('Sexo invalido, informe o seu sexo novamente:  ')).upper()
print(f'Sexo [{sexo}] registrado com sucesso!!')


