n = int(input("Digite um número para saber se é primo ou não: "))
if n / 1 == n and n / n == 1 and n % 2 != 0 and n % 3 != 0:
    print("O número {} é primo".format(n))
else:
    print("O número {} não é primo".format(n))