import requests
import json
# Tehtävä 12.2

'''Tutustu avoimeen OpenWeather-säärajapintaan: https://openweathermap.org/api.
    Kirjoita ohjelma, joka kysyy käyttäjältä paikkakunnan nimen ja tulostaa sitä vastaavan säätilan tekstin
    sekä lämpötilan Celsius-asteina. Perehdy rajapinnan dokumentaatioon riittävästi.

    Palveluun rekisteröityminen on tarpeen, jotta saat rajapintapyynnöissä tarvittavan API-avaimen (API key).
    Selvitä myös, miten saat Kelvin-asteet muunnettua Celsius-asteiksi.'''

def main():

    haku = input("Minkä paikkakunnan säätilaa haetaan? (Esim. Helsinki)\n")
    aste = input("Haluaisitko lämpötilan Celsius-asteina vai Kelvin-asteina? (C/K)\n").upper()
    if aste == "C":
        haettava_aste = "metric"

    else:
        haettava_aste = "imperial"

    pyynto = f"https://api.openweathermap.org/data/2.5/weather?q={haku}" \
             f"&appid=858ea62e6b3e3a6f2991edf5dc7282e0" \
             f"&units={haettava_aste}"
    vastaus = requests.get(pyynto).json()

    print()

    saatila = vastaus['weather'][0]['description']
    lampotila = vastaus['main']['temp']

    print(f"Paikkakunta: {haku}\nSäätila: {saatila}")
    if aste == "C":
        print(f"Lämpötila: {lampotila}ºC")
    else:
        print(f"Lämpötila: {lampotila}ºK")


main()
