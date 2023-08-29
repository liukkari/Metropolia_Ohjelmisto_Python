import random

arvottu_luku = random.randint(1, 10)
while True:
    arvaus = int(input("Arvaa luku 1-10.\n"))
    if arvaus == arvottu_luku:
        print("Oikein!")
        break
    elif arvaus < arvottu_luku:
        print("Liian pieni arvaus.")
        print()
    else:
        print("Liian suuri arvaus.")
        print()
