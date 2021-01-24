linha = "=-" * 15
linha1 = "-" * 30
nota100 = 0
nota50 = 0
nota20 = 0
nota10 = 0
nota1 = 0
print(linha)
print("Bem vindo ao BanCU")
print(linha)
print("VALOR MÁXIMO PARA SAQUE: R$1999")
valor = int(input("Qual valor você deseja sacar? R$"))
print(linha1)
while valor > 1999:
    print(linha1)
    print("VALOR MÁXIMO PARA SAQUE: R$1999")
    valor = int(input("Qual valor você deseja sacar? R$"))
    print(linha1)
while valor >= 100 and nota100 < 6:
        valor = valor - 100
        nota100 += 1
while valor >= 50 and nota50 < 20:
    valor = valor - 50
    nota50 += 1
while valor >= 20 and nota20 < 15:
    valor = valor - 20
    nota20 += 1
while valor >= 10:
    valor = valor - 10
    nota10 += 1
while valor >= 1:
    valor = valor - 1
    nota1 += 1
print(f"Total de {nota100} notas de R$100")
print(f"Total de {nota50} notas de R$50")
print(f"Total de {nota20} notas de R$20")
print(f"Total de {nota10} notas de R$10")
print(f"Total de {nota1} notas de R$1")
print(linha)
print("Volte sempre ao BanCU")
print(linha)
