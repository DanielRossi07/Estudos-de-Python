import random
numeros = (random.randint(0,10), random.randint(0,10), random.randint(0,10), random.randint(0,10), random.randint(0,10))
maior = numeros[0]
menor = numeros[0]

for c in range(0, numeros.__len__()):
    if numeros[c] < menor:
        menor = numeros[c]

for c in range(0, numeros.__len__()):
    if numeros[c] > maior:
        maior = numeros[c]

print(f'Os números sorteados foram: ', end='')
for c in numeros:
    print(f'{c} ', end='')

print(f'\nO maior número foi: {maior}')
print(f'O menor número foi: {menor}')
#print(f'O maior número foi: {max(numeros)}')
#print(f'O menor número foi: {min(numeros)}')