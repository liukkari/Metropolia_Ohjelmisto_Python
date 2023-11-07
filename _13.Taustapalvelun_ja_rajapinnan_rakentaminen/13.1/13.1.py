import json
from flask import Flask

# Tehtävä 13.1

'''Toteuta Flask-taustapalvelu, joka ilmoittaa, onko parametrina saatu luku alkuluku vai ei.
    Hyödynnä toteutuksessa aiempaa tehtävää, jossa alkuluvun testaus tehtiin.
    Esimerkiksi lukua 31 vastaava GET-pyyntö annetaan muodossa: http://127.0.0.1:3000/alkuluku/31.
    Vastauksen on oltava muodossa: {"Number":31, "isPrime":true}.'''


app = Flask(__name__)
@app.route('/alkuluku/<luku>')
def alkuluku(luku):
    luku = int(luku)

    vastaus = {
        "number": luku,
        "isPrime": True
    }

    if luku == 2:
        vastaus = {
            "number": luku,
            "isPrime": True
        }

    else:
        for numero in range(2, int(luku**0.5) + 1):
            if luku % numero == 0:
                vastaus= {"number": luku, "isPrime": False}

    return json.dumps(vastaus)


if __name__ == "__main__":
    app.run(use_reloader=True, port=3001)
