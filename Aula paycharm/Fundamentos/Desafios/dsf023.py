print(f'='*10,'Desafio 023', '='*10)
#loop de erro
sexo = ''
while sexo != 'M' and sexo != 'F':
    sexo = str(input('Digite o sexo [M/F]: ')).upper()
    if sexo != 'M' and sexo != 'F':
        print('Digite apenas M ou F')

print(f'voce é {sexo}')
