salario = int(input("Digite o seu sálario atual: "))
aumento = salario * 1.1
aumento1 = salario * 1.15
if salario >= 1250:
    print("Seu novo sálario é: {:.2f}".format(aumento))
else:
    print("Seu novo sálario é: {:.2f}".format(aumento1))