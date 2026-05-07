#Sorteio de nomes

#biblioteca responsavel por escolher aleatoriamente um item listado
import random
print(f'='*10,'Desafio 013', '='*10)
nome1 = str(input('Digite o nome do primeiro nome: '))
nome2 = str(input('Digite o nome do segundo nome: '))
nome3 = str(input('Digite o nome do terceiro nome: '))
nome4 = str(input('Digite o nome do quarto nome: '))

#listas sao definidas por [variavel1, variavel2]
lista = [nome1, nome2, nome3, nome4]
escolhido = random.choice(lista) #random.choice usado para escolher um item da lista

print(escolhido)