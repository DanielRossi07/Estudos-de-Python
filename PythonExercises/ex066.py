numeros = int(input("Digite quantos números quiser e insira [999] quando quiser parar: "))
contador = 1
somador = numeros

while numeros != 999:
    numeros = int(input("Digite outro valor: "))
    if numeros == 999:
        break
    contador += 1
    somador += numeros

print("Você digitou {} números e a soma deles é {}.".format(contador, somador))