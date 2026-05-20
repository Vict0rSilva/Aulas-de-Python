print(f'='*10,'Desafio 030', '='*10)
#TUPLAS
while True:
    entrada = int(input('Digite um numero entre 0 e 20: '))
    if entrada < 0 or entrada > 20:
        entrada = int(input('Erro: Digite um numero entre 0 e 20: '))
    tupla = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')
    print(tupla[entrada])
    break
