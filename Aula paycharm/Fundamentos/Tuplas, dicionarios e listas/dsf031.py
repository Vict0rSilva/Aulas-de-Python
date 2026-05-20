from random import randint
print(f'='*10, 'Desafio 31', '='*10)
#numeros aleatorios

tupla = (randint(1,10), randint(1,10), randint(1,10), randint(1,10), randint(1,10))


for n in tupla:
    print(f'{n}', end=' ')
print(f'\no maior valor sorteado foi {max(tupla)}')
print(f'o menor valor sorteado foi {min(tupla)}')



