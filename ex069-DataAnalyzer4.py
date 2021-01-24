linha = "-" * 30
pessoasmaior18 = 0
homens = 0
mulhermenor20 = 0

while True:
    print(linha)
    print("CADASTRE UMA PESSOA")
    print(linha)
    idade = int(input("Idade: "))
    sexo = input("Sexo: [M/F] ").upper()
    if idade > 18:
        pessoasmaior18 += 1
    if sexo == "M":
        homens += 1
    if sexo == "F" and idade < 20:
        mulhermenor20 += 1
    print(linha)
    resp = input("Quer continuar? [S/N] ").upper()
    if resp == "Não" or resp == "NÃO" or resp == "N":
        print(linha)
        print(f"Pessoas com mais de 18 anos: {pessoasmaior18}")
        print(f"Homens cadastrados: {homens}")
        print(f"Mulheres com menos de 20 anos: {mulhermenor20} ")
        print(linha)
        break
