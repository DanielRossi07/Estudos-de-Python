nome = input("Qual seu nome? ")
idade = int(input("Qual a sua idade? "))

if idade <= 9:
    print("A sua categoria é MIRIM, {}.".format(nome))
elif idade > 9 and idade <= 14:
    print("A sua categoria é INFANTIL, {}.".format(nome))
elif idade > 14 and idade <= 19:
    print("A sua categoria é JUNIOR, {}.".format(nome))
elif idade == 20:
    print("A sua categoria é SÊNIOR, {}.".format(nome))
elif idade > 20:
    print("A sua categoria é MASTER, {}.".format(nome))