import mysql.connector

connection = mysql.connector.connect(
            host='127.0.0.1',
            port=3306,
            database="flight_game",
            username="root",
            password="4991",
            autocommit=True
)


def fetch_database(search):
    sql = f"SELECT name, municipality FROM airport where ident='{search}'"
    cursor = connection.cursor()
    cursor.execute(sql)
    result = cursor.fetchone()
    print(result)

    name = result[0]
    municipality = result[1]

    return name, municipality
