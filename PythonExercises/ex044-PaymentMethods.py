preço = float(input("Digite o valor do produto: "))
formapagamento = int(input("Digite o número que corresponda a sua forma de pagamento, sendo que suas opções são:\n1 - Á vista no Dinheiro ou Cheque: \n2 - Á vista no Cartão: \n3 - Em até 2x no Cartão: \n4 - Em 3x ou mais no Cartão: \nOpção de pagamento número:  "))
desconto = preço * 0.9
desconto1 = preço * 0.95
juros = preço * 1.2

if formapagamento == 1:
    print("Com essa forma de pagamento você tem desconto de 10%, o valor á ser pago é de {}R$".format(desconto))
elif formapagamento == 2:
    print("Com essa forma de pagamento você tem desconto de 5%, o valor á ser pago é de {}R$".format(desconto1))
elif formapagamento == 3:
    print("Com essa forma de pagamento você não tem descontos e nem juros, o valor á ser pago é de {}R$".format(preço))
elif formapagamento == 4:
    print("Com essa forma de pagamento você pagará juros de 20%, o valor á ser pago é de {}R$".format(juros))
else:
    print("Opção inválida.")