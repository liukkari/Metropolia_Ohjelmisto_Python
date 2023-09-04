import random

maara = int(input("Anna arvottavien pisteiden määrä.\n"))

N = maara
n = 0

while maara != 0:

    x = random.uniform(-1.00, 1.00)
    y = random.uniform(-1.00, 1.00)

    if (x**2 + y**2) < 1:
        n += 1

    maara -= 1

likiarvo = (4*n) / N
print(f"Piin likiarvo on {likiarvo}")