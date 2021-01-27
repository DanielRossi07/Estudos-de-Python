lista = []
resp = "s"

while resp == "s":
    numero = int(input("Digite um número: "))
    if numero not in lista:
        lista.append(numero)
        print("Número adicionado com sucesso...")
    else:
        print("Número duplicado! Não vou adicionar...")
    resp = input("Deseja continuar? [S/N] ").lower()
print("=-=" * 14)
lista.sort()
print(f"Você digitou os valores {lista}")
