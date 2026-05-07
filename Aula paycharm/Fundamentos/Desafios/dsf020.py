print(f'='*10,'Desafio 020', '='*10)
#soma de todos os numeros impares e identificar se sao multiplos de 3

soma = 0
for i in range(1, 501,2 ):
    if i % 3 == 0:
        soma += i
print(soma)

