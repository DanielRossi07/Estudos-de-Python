numero1 = input("Digite o primeiro número: ")
numero2 = input("Digite o segundo número: ")
numero3 = input("Digite o terceiro número: ")
menor = numero1
maior = numero1
#Valida se o primeiro é menor que o segundo e guarda o menor
if menor <= numero2:
    menor = numero1
else:
    menor = numero2

#Valida se o menor é menor que o terceiro e guarda o menor
if menor <= numero3:
    menor = menor
else:
    menor = numero3
#Menor número já foi guardado em "menor"

#Valida se o primeiro número é maior que o segundo e guarda o maior
if maior >= numero2:
    maior = numero1
else:
    maior = numero2

#Valida se o maior é maior que o terceiro e guarda o maior
if maior >= numero3:
    maior = maior
else:
    maior = numero3
#Maior número já foi guardado em "maior"

#Mostra os resultados
print("Entre os números {}, {} e {}:".format(numero1, numero2, numero3))
print("O menor número é: {}".format(menor))
print("O maior número é: {}".format(maior))
