n = int(input("Digite um número para ver a sequência de Fibonacci: "))
primeiro = 0
segundo = 1
resultado = 0

while n != 0:
    print(resultado)
    resultado = primeiro + segundo
    primeiro = segundo
    segundo = resultado
    n = n - 1
