import requests


# Tehtävä 12.1

'''Kirjoita ohjelma, joka hakee ja tulostaa satunnaisen Chuck Norris -vitsin käyttäjälle.
    Käytä seuravalla sivulla esiteltävää rajapintaa: https://api.chucknorris.io/.
    Käyttäjälle on näytettävä pelkkä vitsin teksti.'''


def main():

    tehtava = "https://api.chucknorris.io/"
    path = "jokes/random"
    pyyntö = tehtava + path

    print()
    vastaus = requests.get(pyyntö).json()
    print(vastaus['value'])

main()
