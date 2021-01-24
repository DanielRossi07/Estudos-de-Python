"""numeros = int(input("Digite quantos números quiser e insira [999] quando quiser parar: "))
contador = 0
somador = numeros - 999

while numeros != 999:
    numeros = int(input("Digite outro valor: "))
    contador += 1
    somador += numeros

print("Você digitou {} números e a soma deles é {}.".format(contador, somador))"""

numeros = int(input("Digite quantos números quiser e insira [999] quando quiser parar: "))
contador = 1
somador = numeros

while True:
    numeros = int(input("Digite outro valor: "))
    if numeros == 999:
        break
    contador += 1
    somador += numeros

print("Você digitou {} números e a soma deles é {}.".format(contador, somador))