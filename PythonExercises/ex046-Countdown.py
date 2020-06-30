import time
from playsound import playsound
print("Contagem regrassiva para os fogos de artifício!")
for c in range(3, -1, -1):
    time.sleep(1)
    print(c)
print("Booooom")
playsound(r"C:\Users\UNIVERSO\PycharmProjects\First\Fogos.mp3")