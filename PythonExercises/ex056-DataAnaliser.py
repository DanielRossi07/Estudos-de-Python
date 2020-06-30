mediaidade = 0
mulhervelha = 0
homemvelho = 0
mulhermenos20 = 0
sexom = 0
sexof = 0
nomemaisvelho = ""

#Loop para recolher informações + media da idade
for c in range(1, 5):
    print("---- {}ª Pessoa ----".format(c))
    nome = str(input("Nome: ")).title().strip()
    idade = int(input("Idade: "))
    sexo = str(input("Sexo F/M: ")).upper().strip()
    mediaidade += idade

#Calcula o numero de mulher, homens e mulheres menor de 18 anos
    if sexo == "F":
        sexof += 1
    if sexo == "M":
        sexom += 1
    if sexo == "F" and idade <= 18:
        mulhermenos20 += 1

#Calcula a mulher mais velha
    if c == 1:
        mulhervelha = idade
    else:
        if sexo == "F":
            if idade >= mulhervelha:
                mulhervelha = idade

#Calcula o homem mais velho
    if c == 1:
        homemvelho = idade
        nomemaisvelho = nome
    else:
        if sexo == "M":
            if idade >= homemvelho:
                homemvelho = idade
                nomemaisvelho = nome

#Mostra as informações
print("A media de idade do grupo é de {}.".format(mediaidade / 4))
print("No grupo tem {} homens, o homem mais velho tem {} e se chama {}.".format(sexom, homemvelho, nomemaisvelho))
print("No grupo tem {} mulheres e {} abaixo de 18 anos.".format(sexom, mulhermenos20))