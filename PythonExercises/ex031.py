tamanhoviagem = int(input("Qual a distância da sua viagem em Km? "))
valor = tamanhoviagem * 0.5
valor1 = tamanhoviagem * 0.45
print("Viagens de até 200Km serão cobradas o valor de 50 centavos por Km!")
print("Viagens de mais de 200Km serão cobradas o valor de 45 centavos por Km!")
if tamanhoviagem <= 200:
    print("O valor da passagem para uma viagem de {}Km é de {}R$!".format(tamanhoviagem, valor))
else:
    print("O valor da passagem para uma viagem de {}Km é de {}R$!".format(tamanhoviagem, valor1))
print("!!! Boa Viagem !!!")