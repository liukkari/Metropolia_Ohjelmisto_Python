import numpy

# Tehtävä 1.1: Tehtävä 1. Muunna asteiksi.

rad = 1.35
print(numpy.degrees(rad))

rad = 2.765
print(numpy.degrees(rad))
print()

# Tehtävä 1.1: Tehtävä 2. Muunna radiaaneiksi

aste = 137.7
print(numpy.radians(aste))

aste = 62.3
print(numpy.radians(aste))
print()

''' Tehtävä 1.1: Tehtävä 3.
 Laadi taulukko, hosta esittää seuraavat kulmat radiaaneina'''

lista = numpy.array([30, 45, 60, 120, 135,
                     150, 180, 270, 360])

for i in lista:
    print(numpy.radians(i))

''' Tehtävä 2.2.1: Tehtävä 1.
 Suorakulmaisen kolmion kateetit ovat 1,6m ja 2,3m.
 Kuinka pitkä on hypotenuusa?'''


# a= 1.6m ja b= 2.3m
a = numpy.array([1.6])
b = numpy.array([2.3])


c = numpy.sqrt(numpy.square(a) + numpy.square(b))

print(f"Hypotenuusan pituus on: {c[0]}m")
