#Adivinhar numero da maquina
#melhorando com WHILE
from random import randint #gera um numero interio aleatorio
print(f'='*10,'Desafio 024', '='*10)
print('Descubra qual o numero aleatorio entre 1 e 10')

escolha = ''
aleatorio = randint(1, 10)
tentativas = 1
while escolha != aleatorio:
    escolha = int(input('Digite um numero inteiro entre 1 e 10: '))

    if escolha != aleatorio:
        print(f'Voce errou o numero, tente novamente')
        tentativas += 1

print(f'Nossa, voce acertou!! O numero foi {aleatorio} voce tentou {tentativas}x')