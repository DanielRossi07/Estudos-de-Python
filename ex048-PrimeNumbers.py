print("Números primos de 1 á 500!")
n = 0
for c in range(1, 500):
    if c % 3 == 0 and c % 2 != 0:
        print(c)
        n = n + c
print(n)
