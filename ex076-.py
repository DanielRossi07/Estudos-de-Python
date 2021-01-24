"""lista = ('Lápis', 0.50, 'Caneta', 1, 'Caderno', 10, 'Livro', 15, 'Estojo', 5.50)
linha = "-" * 40
print(linha)
print('Listagem de Preços')
print(linha)

for c in range(0, len(lista)):
    if c % 2 == 0:
        cont = 29 - len(lista[c])
        print(lista[c], "." * cont, end= " R$ ")
    else:
        print("{:.2F}".format(lista[c]))"""


lista = ('Lápis', 0.50, 'Caneta', 1, 'Caderno', 10, 'Livro', 15, 'Estojo', 5.50)
linha = "-" * 40
print(linha)
print(f'{"Lista de Produtos":^40}')
print(linha)

for c in range(0, len(lista)):
    if c % 2 == 0:
        print(f'{lista[c]:.<30}', end= "")
    else:
        print(f'R${lista[c]:>7.2F}')
print(linha)
