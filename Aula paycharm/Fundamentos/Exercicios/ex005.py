#Importar bibliotecas
#https://docs.python.org/pt-br/3.14/library/math.html
#import math 'importar toda biblioteca'
from math import sqrt, floor #importa apenas uma parte da biblioteca

numero = int(input('Digite um numero: '))
raiz = sqrt(numero)
print(f'A raiz de {numero} é {raiz:.2f}')#arrendodar para cima {math.ceil(raiz)} ciel para cima e floor para baixo