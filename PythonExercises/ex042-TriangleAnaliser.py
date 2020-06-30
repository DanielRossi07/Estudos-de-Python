a = int(input("Digite o primeiro lado do triângulo: "))
b = int(input("Digite o segundo lado do triângulo: "))
c = int(input("Digite o terceiro lado do triângulo: "))
maior = a
medio = a
menor = a

#Validando maior número
if maior >= b: #Verifica se "A" maior que "B" e guarda o maior
    maior = maior
else:
    maior = b

if maior >= c: #Verifica se "maior" é maior que "C" e guarda o maior
    maior = maior
else:
    maior = c
#Maior número validado


#Validando menor número
if menor <= b:
    menor = menor
else:
    menor = b

if menor <= c:
    menor = menor
else:
    menor = c
#Menor número validado


#Validando número médio
if medio >= b and medio <= c or medio >= c and medio <= b:
    medio = medio
else:
    medio = b

if medio >= a and medio <= c or medio >= c and medio <= a:
    medio = medio
else:
    medio = c
#Número médio validado


#Mostra resultados
print("O maior número é {}: ".format(maior))
print("O médio número é {}: ".format(medio))
print("O menor número é {}: ".format(menor))

if menor + medio > maior:
    print("É possivel a contrução do triângulo com essas dimenções: {}, {}, {}!".format(a, b, c))
    if menor == medio and menor == maior:
        print("O triângulo é Equilátero!")
    elif menor == medio or menor == maior or medio == maior:
        print("O triângulo é Isósceles!")
    elif menor != medio and menor != maior:
        print("O triângulo é Escaleno!")
else:
    print("Não é possivel a construção do triângulo com essas dimenções: {}, {}, {}!".format(a, b, c))
