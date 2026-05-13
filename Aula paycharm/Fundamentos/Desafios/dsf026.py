print(f'='*10,'Desafio 026', '='*10)
#utilizando BREAK
flag = 0
soma = 0
while True:
    numero = int(input('Digite um numero (digite 999 para parar): '))
    if numero == 999:
        break
    soma = numero + numero
    flag += 1
print(f'voce digitou {flag} numeros e a soma foi de {soma}')

