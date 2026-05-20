tupla = ('Caneta', 2.5, 'lapis', 3.00)


for n in range(0, len(tupla)):
    if n % 2 == 0:
        print(f'{tupla[n]:.<30}', end='')
    else:
        print(f'R${tupla[n]:>3}')


