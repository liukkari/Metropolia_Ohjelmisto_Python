from math import pi


def hinta_laskuri(halkaisija, hinta):
    sade = (halkaisija/2) * 0.01  # Lasketaan halkaisijasta säde ja muutetaan metreiksi
    print(sade)
    pinta_ala = pi*sade**2
    print(pinta_ala)

    nelio_hinta = hinta / pinta_ala
    return nelio_hinta


def main():
    print("Anna kahden pizzan halkaisija (cm) ja hinnat (e). \n")
    ekan_pizzan_koko = float(input("Ensimmäisen pizzan koko? (cm)\n"))
    ekan_pizzan_hinta = float(input("Ensimmäisen pizzan hinta? (e)\n"))
    print()
    toisen_pizzan_koko = float(input("Toisen pizzan koko? (cm)\n"))
    toisen_pizzan_hinta = float(input("Toisen pizzan hinta? (e)\n"))

    eka_pizza = hinta_laskuri(ekan_pizzan_koko, ekan_pizzan_hinta)
    toka_pizza = hinta_laskuri(toisen_pizzan_koko, toisen_pizzan_hinta)
    print(eka_pizza)
    print(toka_pizza)

    if eka_pizza < toka_pizza:
        print(f"Ensimmäinen pizza on edullisempi hinnaltaan: {eka_pizza:0.2f} m**2/e")
    elif eka_pizza == toka_pizza:
        print(f"Molemmat ovat samanhintaisia hinnaltaan: {eka_pizza:0.2f} m**2/e")
    else:
        print(f"Toka pizza on edullisempi hinnaltaan: {toka_pizza:0.2f} m**2/e")


main()
