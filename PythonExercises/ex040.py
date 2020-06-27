nota = float(input("Digite sua primeira nota: "))
nota1 = float(input("Digite a segunda nota: "))
media = (nota + nota1) / 2
print("Se sua média for menor que 5 você será REPROVADO\n Se sua média for menor que 7 você estará de RECUPERAÇÃO\n Se sua média for maior ou igual 7, você será APROVADO!")
if media >= 5 and media <= 6.9:
    print("Sua média foi {}, você está de recuperação!".format(media))
elif media < 5:
    print("Sua média foi {}, você foi reprovado!".format(media))
elif media > 6.9:
    print("Sua média foi {}, você foi aprovado!".format(media))