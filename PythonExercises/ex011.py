l = float(input("Qual a largura da parede? "))
a = float(input("E qual a altura da parede? "))
area = float(a * l)
litros = float(area / 2)
print("Para pintar a área de {}m² você vai precisar de {} litros de tinta!".format(area, litros))
