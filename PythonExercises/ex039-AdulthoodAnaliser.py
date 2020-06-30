from datetime import date
#Improvements to be done
#dia = input("Qual o dia do seu nascimento? ")
#mes = input("Qual o mês do seu nascimento? (Em forma numérica, por favor!) ")
ano = int(input("Qual o ano do seu nascimento? "))
atual = date.today().year
idade = atual - ano
anocerto = ano + 18
passou = idade - 18
faltam = anocerto - atual
if idade > 18:
    print("Você já deveria ter se alistado em {}, já se passaram {} anos!".format(anocerto, passou))
elif idade < 18:
    print("Você deverá se alistar em {}, faltam {} anos!".format(anocerto,faltam))
elif idade == 18:
    print("Você deve se alistar NESSE ano")
