print(f'='*10,'Desafio 028', '='*10)
#jogar par ou impar com a maquina
from random import randint

flag = 0
while True:
    numero = int(input('Diga um valor: '))
    maquina = randint(1, 10)
    print('-'* 25)
    escolha = str(input('Par ou Impar (P/I): ')).upper()
    if (maquina + numero) % 2 == 0 and escolha == 'P':
        print(f'A maquina jogou {maquina} e voce {numero} = {maquina+numero} PAR!! VAMOS DE NOVO!')
        flag += 1
        print('-=' * 25)
    elif (maquina + numero) % 2 == 1 and escolha == 'I':
        if escolha == 'I':
            print(f'A maquina jogou {maquina} e voce {numero} = {maquina+numero} IMPAR!! VAMOS DE NOVO!')
            flag += 1
            print('-=' * 25)
    else:
        print(f'A maquina jogou {maquina} e voce {numero} = {maquina+numero} Voce perdeu!')
        break
print('-=' * 25)
print(f'Voce ganhou {flag}x')