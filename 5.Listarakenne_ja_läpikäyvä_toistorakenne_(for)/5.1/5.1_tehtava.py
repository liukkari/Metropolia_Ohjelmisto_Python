import random

lista = []

arpakuutioiden_lukumäärä = int(input("Anna arpakuutioiden lukumäärä.\n"))
print()

for i in range(arpakuutioiden_lukumäärä):
    arpaluku = random.randint(1, 6)
    print(arpaluku)

