linha = "-" * 30
total = 0
maior1000 = 0
nomemaisbarato = ""
menorpreço = 0

print(linha)
print("LOJA SUPER BARATINHA")
print(linha)
while True:
    nome = input("Nome do Produto: ").capitalize()
    preço = int(input("Preço: R$"))
    print(linha)
    total = total + preço
    if nomemaisbarato == "":
        nomemaisbarato = nome
    if menorpreço == 0:
        menorpreço = preço
    if preço < menorpreço:
        nomemaisbarato = nome
    if preço > 1000:
        maior1000 += 1
    resp = input("Deseja continuar? [S/N] ").upper()
    print(linha)
    if resp[0] != "S":
        print(f"Total da compra foi: {total}")
        print(f"Produtos custando mais que R$1000: {maior1000}")
        print(f"Produto mais barato: {nomemaisbarato} por {menorpreço}")
        linha
        break