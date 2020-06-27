#Soma os números pares inseridos pelo usuário
total = 0
for c in range(0, 6):
    n = int(input("Digite um número inteiro: "))
    if n % 2 == 0:
        total = total + n
print("a soma dos números pares é {}".format(total))