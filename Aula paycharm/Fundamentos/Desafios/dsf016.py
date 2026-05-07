#Numero par ou impar
print(f'='*10,'Desafio 016', '='*10)

numero = int(input('Digite um numero para descobrir se é par ou impar: '))

if numero % 2 == 0:
    print(f'{numero} é PAR')
else:
    print(f'{numero} e IMPAR')