numeros = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')
resp = -1

while resp < 0 or resp > 20:
    resp = int(input('Digite um número entre 0 e 20: '))

numero = numeros[resp].capitalize()
print(f'Você digitou o número {numero}')
