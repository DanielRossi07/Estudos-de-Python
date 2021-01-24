salario = float(input("Qual o seu salário? "))
aumento = float(input("Qual o aumento desejado?"))
porcento = aumento * 0.01
salario_aumentado = salario * porcento
salario_atualizado = salario * (1 + porcento)
print("O aumento foi de {:.2f}, e seu salario atualizado é: {:.2f}".format(salario_aumentado, salario_atualizado))
