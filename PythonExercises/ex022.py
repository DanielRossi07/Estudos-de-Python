nome = input("Digite seu nome: ")
nomeupper = nome.upper()
nomelower = nome.lower()
nometitle = nome.title()
espaços = nome.count(" ")
primeironome = (nome.split()[0]).__len__()
nomesemespaço = nome.__len__() - espaços
print("Seu nome em maiusculo é {}!".format(nomeupper))
print("Seu nome em minusculo é {}!".format(nomelower))
print("Seu primeiro nome tem {} letras!".format(primeironome))
print("Tamanho sem espaço: {}".format(nomesemespaço))
