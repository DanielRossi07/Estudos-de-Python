numeros = (int(input("Digite um número: ")), int(input("Digite outro número: ")), int(input("Digite mais um número: ")), int(input("Digite o último número: ")))

if 9 in numeros:
    print(f"O número 9 apareceu {numeros.count(9)} vezes.")
else:
    print("O número 9 não foi encontrado!")

if 3 in numeros:
    print(f"O número 3 apareceu a primeira vez na {numeros.index(3) + 1}ª posição.")
else:
    print("O número 3 não foi encontrado!")

print("Os números pares foram: ", end="")
for c in range(0, numeros.__len__()):
    if numeros[c] % 2 == 0:
        print(numeros[c], end=" ")