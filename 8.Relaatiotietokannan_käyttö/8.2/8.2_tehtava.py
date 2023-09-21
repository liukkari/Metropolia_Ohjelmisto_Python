import mysql.connector

connection = mysql.connector.connect (

    host="127.0.0.1",
    port=3307,
    database="flight_game",
    username="root",
    password="4991",
    autocommit=True

)


def hakukone(koodi):
    sql = "SELECT type FROM airport"
    sql += " WHERE iso_country = '" + koodi + "'"

    cursor = connection.cursor()
    cursor.execute(sql)
    tulos = cursor.fetchall()

    small = 0
    medium = 0
    big = 0
    helix = 0

    if cursor.rowcount > 0:
        for koko in tulos:
            if "small_airport" in koko:
                small += 1
            elif "medium_airport" in koko:
                medium += 1
            elif "seaplane_base" in koko:
                big += 1
            elif "heliport" in koko:
                helix += 1

    return small, medium, big, helix


def main():
    maakoodi = input("Anna maakoodi.(Esim. FI)\n")
    pieni, medium, iso, heli = hakukone(maakoodi)

    if pieni == 0 and iso == 0 and heli == 0:
        print("Ei tuloksia.")
    else:
        print(f"Pieniä lenttokenttiä on: {pieni}, "
              f"Keskikokoisia lentokenttiä on: {medium}, "
              f"Isoja lentokenttiä on: {iso}"
              f" ja helikopterikenttiä on: {heli}.")


main()
