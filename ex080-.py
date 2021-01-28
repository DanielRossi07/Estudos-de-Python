lista = []

for c in range(0,5):
    numero = int(input("Digite um número: "))
    if len(lista) == 0:
        lista.append(numero)
        print("O número adicionado no começo da lista")
    elif numero >= lista[len(lista) - 1]:
        lista.append(numero)
        print(f"Número adicionado na posição {lista.index(numero)}")
    else:
        for c in range(0, len(lista)):
            if numero <= lista[c]:
                lista.insert(c, numero)
                print(f"Número adicionado na posição {lista.index(numero)}")
                break
print(lista)