print("Você terá que digitar dois números para saber mais opções...")
n = int(input("Digite o primeiro número: "))
n1 = int(input("Digite o segundo número: "))
print("--- Lista de opções! ---\n[1] Somar\n[2] Multiplicar\n[3] Maior\n[4] Novos números\n[5] Sair do programa")
r = 0
resultado = 0


while r != 1 and r != 2 and r != 3 and r != 4 and r != 5:
    r = int(input("Faça sua escolha: "))
    while r == 4:
        n = int(input("Digite o primeiro número novamente: "))
        n1 = int(input("Digite o segundo número novamente: "))
        print("--- Lista de opções! ---\n[1] Somar\n[2] Multiplicar\n[3] Maior\n[4] Novos números\n[5] Sair do programa")
        r = int(input("Faça sua escolha: "))

    if r == 1:
        resultado += n + n1
        print("Os números {} e {} somados dão {}.".format(n, n1, resultado))
    if r == 2:
        resultado += n * n1
        print("Os números {} e {} Multiplicados dão {}.".format(n, n1, resultado))
    if r == 3:
        if n > n1:
            print("Entre os números {} e {} o maior é {}.".format(n, n1, n))
        elif n1 > n:
            print("Entre os números {} e {} o maior é {}.".format(n, n1, n1))
        elif n == n1:
            print("Os números {} e {} são iguais.".format(n, n1))
    if r == 5:
        exit()


