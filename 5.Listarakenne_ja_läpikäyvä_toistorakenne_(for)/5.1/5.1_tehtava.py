import random

lista = []

arpakuutioiden_lukumäärä = int(input("Anna arpakuutioiden lukumäärä.\n"))
print()

summa = 0
for i in range(arpakuutioiden_lukumäärä):
    arpaluku = random.randint(1, 6)
    summa += arpaluku
    print(f"Tämän hetkinen noppien summa on {summa}")


