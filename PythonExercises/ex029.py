print("!!! O limite de velocidade é 80Km/H !!!")
velocidade = int(input("Qual a velocidade do carro? "))
excedente = velocidade - 80
multa = excedente * 7
multiplicador = 7
if velocidade > 80:
    print("O seu carro estava {}KM/H acima do limite e foi multado. Sua multa é de: {}R$!".format(excedente, multa))
    print("O valor da multa é de {}R$ por KM/H excedido.".format(multiplicador))
else:
    print("Parabéns, continue dentro do limite!")
