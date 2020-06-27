valorcasa = float(input("Qual o valor do imóvel que deseja comprar? "))
salario = float(input("Qual o seu salário atual? "))
anos = int(input("Em quantos anos pretende pagar a casa? "))
parcela = valorcasa / (anos * 12)
print("-=-" * 30)
if parcela > (salario * 0.3):
    print("Você não pode comprar esse imóvel, pois o valor da parcela seria {:.2f}R$, e ultrapassa 30% do seu salário!".format(parcela))
else:
    print("Com um salário de {}R$, você pode comprar a casa escolhida, e sua parcela será de {:.2f}R$ por mês!".format(salario, parcela))