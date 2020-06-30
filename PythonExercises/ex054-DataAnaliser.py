from datetime import date
atual = date.today().year
contadornovo = 0
contadorvelho = 0
for c in range(1, 8):
    ano = int(input("Em que ano a {}ª pessoa nasceu? ".format(c)))
    idade = atual - ano

    if idade >= 18:
        print("A {}ª pessoa tem {} anos e já atingiu maioridade!".format(c, idade))
        contadorvelho += 1
    else:
        print("A {}ª pessoa tem {} anos e ainda não atingiu maioridade!".format(c, idade))
        contadornovo += 1

print("Tivemos {} pesssoas maiores de idade e {} pessoas menores de idade.".format(contadorvelho, contadornovo))