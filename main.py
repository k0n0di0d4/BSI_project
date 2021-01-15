import math
import threading

print("Witaj swicie")
x = 10
y = 20
print(x + y)


def ciezka_praca():
    suma = 0
    for i in range(1_000_000):
        suma += i * i * math.cos(i)
    print(suma)


moj_watek = threading.Thread(target=ciezka_praca)
moj_watek.start()
moj_watek2 = threading.Thread(target=ciezka_praca)
moj_watek2.start()
moj_watek3 = threading.Thread(target=ciezka_praca)
moj_watek3.start()
ciezka_praca()
moj_watek.join()
moj_watek2.join()
moj_watek3.join()
print("koniec programu")
