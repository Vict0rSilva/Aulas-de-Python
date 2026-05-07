#condiçoes

nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))

#condição Simples com apenas um IF sem else
media = (nota1 + nota2) / 2
#if media <=5:
    #print(f'ACHO QUE NÃO PASSA')
#print(f'Sua media foi {media:.1f}')

#Condiçoes simplificada
print('PARABENS' if media >=7 else 'ESTUDE MAIS')

#Condição composta
print(f'Sua media foi {media:.2f}')
if media >= 7:
    print('Sua media foi aprovada')
else:
    print('Sua media foi reprovada')