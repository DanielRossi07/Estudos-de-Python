#Verifica se a frase é um Polídromo ou não
frase = str(input("Digite uma frase: ")).strip().upper()
palavras = frase.split()
junto = "".join(palavras)
reverso = ""
for c in range(len(junto) -1, -1, -1):
    reverso += junto[c]

if junto == reverso:
    print("A frase {} é igual de trás para frente. Temos um Palíndromo!".format(junto))
else:
    print("A frase {} não é igual de trás para frente. Não temos um Palíndromo!".format(junto))
print(junto)
print(reverso)
