from time import sleep
print(f'='*10,'Desafio 025', '='*10)
print('=-'*20)
seletor = 0
while seletor != 5:

    numero1 = int(input('Digite o primeiro valor: '))
    numero2 = int(input('Digite o segundo valor: '))
    print('Digite a opção que deseja\n[1]Somar\n[2]Multiplicar\n[3]Maior valor\n[4]Novos numeros\n[5]Sair')
    seletor = int(input('Digite a opção desejada: '))

    if seletor == 1:
        soma = numero1 + numero2
        print(f'A soma de {numero1} e {numero2} é {soma} ')

    elif seletor == 2:
        multiplicar = numero1 * numero2
        print(f'A multiplicar de {numero1} e {numero2} é {multiplicar} ')

    elif seletor == 3:
        if numero1 > numero2:
            print(f'o maior numero é {numero1}')
        else:
            print(f'o maior numero é {numero2}')
    elif seletor == 4:
        numero1 = int(input('Digite o primeiro valor: '))
        numero2 = int(input('Digite o segundo valor: '))
    else:
        print('opção invalida! Digite novamente')

    print('=-'*20)
    sleep(2)
print('FIM DO PROGRAMA')
