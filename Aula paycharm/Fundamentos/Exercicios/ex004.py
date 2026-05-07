#operadores
#nome = input('digite seu nome ')
#print(f'Olá, {nome:=^20}')
#o sinal de : =^20 significa que ele vai por = entre "^" o nome ou variavel 20 vezes

numero1 = int(input('Digite o primeiro numero: '))
numero2 = int(input('Digite o segundo numero: '))
#forma simpleficada
soma = numero1 + numero2
multiplicar = numero1 * numero2
divisao = numero1 / numero2
divisaointeiro = numero1 // numero2
potencia = numero1 ** numero2

print(f'A soma é {soma} a multiplicação é {multiplicar} a divisao é {divisao}')#,end='' para não quebrar a linha e \n para quebrar a linha
print(f'A divisao inteira é {divisaointeiro} e a potencia é {potencia}\n')
print('Forma funcional\n')
print(f'a soma é {numero1+numero2} a multiplicação é {numero1*numero2} a divisão é {numero2/numero2}\na divisao inteira é {numero1//numero2} e a potencia é {numero1**numero2}')