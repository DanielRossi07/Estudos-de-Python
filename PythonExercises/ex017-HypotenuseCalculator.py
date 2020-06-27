from math import hypot
adj = float(input("Digite o cateto adjacente: "))
opo = float(input("Digite o cateto oposto: "))
#hypo = hypot(adj, opo)
hypo = (adj ** 2 + opo ** 2) ** (1/2)
print("A hypotenusa do cateto {} e oposto {} é {:.2f}".format(adj, opo, hypo))