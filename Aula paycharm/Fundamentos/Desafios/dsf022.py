print(f'='*10,'Desafio 022', '='*10)
#soma de todos os numeros pares e identificar se sao multiplos de 2
soma = 0
lista = []
numeros_pares = 0
for i in range(1, 7):
    numero_digitado = int(input(f'Digite o {i} valor:  '))
    lista.append(numero_digitado)
    if numero_digitado % 2 == 0:
        soma += numero_digitado
        numeros_pares += 1
print(f'os valores digitados foram {lista} que sao {numeros_pares} pares e a soma dos numeros pares é {soma}')