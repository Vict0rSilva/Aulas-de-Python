print(f'='*10,'Desafio 028', '='*10)
#tabuada de x

while True:
    numero = int(input('Deseja ver a tabuada de que valor? '))
    if numero < 0:
        break
    for c in range(1, 11):
        mult = numero * c
        print(f'{numero} x {c} = {mult}')

print('FIM')