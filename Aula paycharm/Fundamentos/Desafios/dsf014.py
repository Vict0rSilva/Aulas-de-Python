#Adin=vinhar numero da maquina
from random import randint #gera um numero interio aleatorio
print(f'='*10,'Desafio 014', '='*10)
print('Descubra qual o numero aleatorio entre 1 e 10')
escolha = int(input('Digite um numero inteiro entre 1 e 10: '))

aleatorio = randint(1,10)

if escolha == aleatorio:
    print(f'Nossa, voce acertou!! O numero foi {aleatorio}')

else:
    print(f'Voce errou o numero foi {aleatorio}, tente novamente')