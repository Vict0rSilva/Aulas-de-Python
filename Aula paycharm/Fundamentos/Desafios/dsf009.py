print(f'='*10,'Desafio 009', '='*10)
print('quanto de tinta para pintar uma parede')
altura = float(input('Qual a altura da parede em metros: '))
largura = float(input('Qual a largura da parede em metros: '))

print(f'uma parede de\nAltura: {altura:.2f}\nLargura: {largura:.2f}\nTem {altura*largura:.2f}m²\nvoce vai precisar de {altura*largura/2:.2f}Litros de tinta')