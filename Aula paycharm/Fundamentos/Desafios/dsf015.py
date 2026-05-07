#Multa por KM a cima do limite
print(f'='*10,'Desafio 015', '='*10)

velocidade = int(input('Qual a velocidade do carro: '))
multa = velocidade - 80
if velocidade > 80:
    print(f'excediu o limite permitido, sua velocidade foi {velocidade}Km/h')
    print(f'multa no valor de R$ {multa*7},00')
else:
    print(f'Sua velocidade foi {velocidade}Km/h')