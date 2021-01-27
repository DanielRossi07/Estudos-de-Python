lista = ('Banana', 'Uva', 'Manga', 'Lixia', 'Morango')
listavogais = ('a', 'e', 'i', 'o', 'u')

for contador in range(0, len(lista)):
    vogais = ""
    for c in range(0, len(lista[contador])):
        for cont in range(0, 5):
            if lista[contador][c].upper() == listavogais[cont].upper():
                vogais +=  " " + listavogais[cont]

    print(f"Na palavra {lista[contador].upper()} temos {vogais}")