from flask import Flask
import json
import tietokanta_haku_13 as tietokanta

# Tehtävä 13.2

'''Toteuta taustapalvelu, joka palauttaa annettua lentokentän ICAO-koodia vastaavan lentokentän nimen
    ja kaupungin JSON-muodossa. Tiedot haetaan opintojaksolla käytetystä lentokenttätietokannasta.
    Esimerkiksi EFHK-koodia vastaava GET-pyyntö annetaan muodossa: http://127.0.0.1:3000/kenttä/EFHK.
    Vastauksen on oltava muodossa: {"ICAO":"EFHK", "Name":"Helsinki Vantaa Airport", "Municipality":"Helsinki"}.'''

app = Flask(__name__)
@app.route("/kenttä/<haku>")
def sivu(haku):

    name, municipality = tietokanta.fetch_database(haku)
    vastaus = {
            "ICAO": haku,
            "Name": name,
            "Municipality": municipality
    }
    return json.dumps(vastaus)


if __name__ == "__main__":
    app.run(use_reloader=True, port=3001)
