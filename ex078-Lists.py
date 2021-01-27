lista = list()
maior = 0
menor = 0
for c in range(0, 5):
    lista.append(int(input(f'Digite um valor para a posição {c}: ')))
    if c == 0:
        maior = menor = lista[c]
    else:
        if maior < lista[c]:
            maior = lista[c]
        if menor > lista[c]:
            menor = lista[c]
print("-=" * 18)
print(f'Você digitou os valores {lista}')
print(f'O maior valor foi {maior} nas posições ', end='')
for i, n in enumerate(lista):
    if n == maior:
        print(f'{i}... ', end='')
print(f'\nO menor valor foi {menor} nas posições ', end='')
for i, n in enumerate(lista):
    if n == menor:
        print(f'{i}... ', end='')