import math

# Tehtävä 2.2

'''Kirjoita ohjelma, joka kysyy ympyrän säteen
    ja tulostaa sen pinta-alan.'''

sade = input("Anna ympyrän säde. (cm)\n")
ympyran_pinta_ala = math.pi * float(sade)**2
print(f"Ympyrän pinta-ala on: {ympyran_pinta_ala:.2f}cm.")