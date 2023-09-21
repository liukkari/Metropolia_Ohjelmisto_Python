import mysql.connector
from geopy import distance

connection = mysql.connector.connect(
        host="127.0.0.1",
        port=3307,
        database="flight_game",
        username="root",
        password="4991",
        autocommit=True
)


def distance_calculator(lasku1, lasku2):
    lasku_generaattori = distance.distance(lasku1, lasku2)
    return lasku_generaattori


def search_generator(eka_koodi, toka_koodi):

    cursor = connection.cursor()

    sql = "SELECT latitude_deg, longitude_deg FROM airport "
    sql += "WHERE ident = '" + eka_koodi + "'"
    cursor.execute(sql)
    eka_tulos = cursor.fetchone()

    sql = "SELECT latitude_deg, longitude_deg FROM airport "
    sql += "WHERE ident = '" + toka_koodi + "'"
    cursor.execute(sql)
    toka_tulos = cursor.fetchall()

    etaisyys = distance_calculator(eka_tulos, toka_tulos)

    return etaisyys


def main():
    eka_icao_koodi = input("Anna ensimmäinen ICAO-koodi. (Esim. TAPA)\n")
    toka_icao_koodi = input("Anna toinen ICAO-koodi. (Esim. AD-0001)\n")

    etaisyys = search_generator(eka_icao_koodi, toka_icao_koodi)
    print(f"Lentokenttien etäisyys toisista on: {etaisyys}")


main()

