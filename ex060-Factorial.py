"""numero = int(input("Digite um número para saber o fatorial: "))
contador = numero - 1
resultado = numero * contador
print("{}x{} = {}".format(numero,contador,resultado))

while contador != 1:
    resultado = resultado * (contador -1)
    contador = contador - 1
    print("{}x{} = {}".format(numero,contador,resultado))

print("O resultado do fatorial do número {} é {}.".format(numero, resultado))"""

numero = int(input("Digite um número para saber o fatorial: "))
contador = numero
resultado = numero

while contador != 1:
    contador = contador - 1
    resultado = resultado * contador
    print("{}x{} = {}".format(numero,contador,resultado))

print("O resultado do fatorial do número {} é {}.".format(numero, resultado))