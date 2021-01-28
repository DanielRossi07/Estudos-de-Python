lista = []

while True:
    numero = lista.append(int(input("Digite um número: ")))
    resp = input("Quer continuar? [S/N] ").lower()
    if resp != "s":
        break
lista.sort(reverse=True)
print(f"Os números digitados foram: {lista}")
print(f"Você digitou {len(lista)} números")
if 5 in lista:
    print(f"O número 5 está na {lista.index(5)}ª posição")
else:
    print("O número 5 não foi encontrado")