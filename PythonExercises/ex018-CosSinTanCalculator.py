from math import sin, cos, tan, radians
ang = float(input("Digite o ângulo: "))
sin = sin(radians(ang))
cos = cos(radians(ang))
tan = tan(radians(ang))
print("O seno do ângulo {} é {} \nO cosseno do ângulo {} é {} \nA tangente do ângulo {} é {}".format(ang, sin, ang, cos, ang, tan))