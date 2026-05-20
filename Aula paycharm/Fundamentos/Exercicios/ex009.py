#Tuplas, variaveis composta
#Toda tupla em ()
#tublas () / listas [] / dicionario {}
#Tuplas sao imutaveis
lanche = ('biscoito', 'bolacha', 'salgado', 'coxinha')
'''print(lanche)
print(lanche[1])#fatiamento
print(lanche[-2])
print(lanche[1:3])
print(lanche[:2])
print(lanche[2:])
print(lanche[:3])'''

print(sorted(lanche)) #ordena a tupla

print(len(lanche))
#maneira 1
for comida in lanche:
    print(comida)
print('-='*20)

#maneira 2
for comida in range(0, len(lanche)):
    #print(lanche[comida])
    print(f'comi {lanche[comida]}')

print('-='*20)
#maneira 3 com posição
for pos, comida in enumerate(lanche):
    print(f'comi {comida} na posição {pos}')
