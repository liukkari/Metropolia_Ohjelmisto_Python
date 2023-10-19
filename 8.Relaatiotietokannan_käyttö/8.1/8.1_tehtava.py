import mysql.connector

# Tehtävä 8.1

'''Kirjoita ohjelma, joka kysyy käyttäjältä lentoaseman ICAO-koodin.
    Ohjelma hakee ja tulostaa koodia vastaavan lentokentän nimen ja sen sijaintikunnan
    kurssilla käytettävästä lentokenttätietokannasta.
    ICAO-koodi on tallennettuna airport-taulun ident-sarakkeeseen.'''

connection = mysql.connector.connect(

    host='127.0.0.1',
    port=3307,
    database='flight_game',
    user="root",
    password='4991',
    autocommit=True

)


def hakukone(icao):
    sql = "SELECT name, municipality FROM airport"
    sql += " WHERE ident='" + icao + "'"

    cursor = connection.cursor()
    cursor.execute(sql)
    rivi = cursor.fetchone()

    if cursor.rowcount > 0:
        lentokentta = rivi[0]
        sijainti = rivi[1]
    else:
        lentokentta = ''
        sijainti = ""

    return lentokentta, sijainti


def main():
    icao_koodi = input("Anna ICAO-koodi.(Esim. TAPA)\n")
    lentokentta, sijainti = hakukone(icao_koodi)

    if len(lentokentta) == 0 or len(sijainti) == 0:
        print("Ei tuloksia.")
    else:
        print(f"ICAO-koodilla: {icao_koodi}, löytyi lentokenttä nimeltä: {lentokentta}"
              f" ja sijaintikunnalla: {sijainti}.")


main()
