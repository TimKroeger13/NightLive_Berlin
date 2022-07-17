from operator import le
from flask import Flask, request, redirect, url_for, render_template, jsonify, after_this_request
import json
import psycopg2
from datetime import datetime


ServerScript = Flask(__name__)
ServerScript.debug = True


@ServerScript.route("/", methods=['GET', 'POST'])
def index():
    if request.method == "POST":
        print()
        print("[SERVER] Data was send to the server")
        data = request.form.getlist("NLBObject")

        JasonServerData = json.loads(data[0])
        print(JasonServerData)
        print(JasonServerData["location"]["coordinates"])

        # DB code
        try:
            connection = psycopg2.connect(user="NLB",
                                          password="selectedSections",
                                          host="localhost",
                                          port="55432",
                                          database="NightliveBerlin")
            cursor = connection.cursor()

            # Get Cords

            latcor = JasonServerData["location"]["coordinates"][0]
            longcor = JasonServerData["location"]["coordinates"][1]

            # Add Data to the database

            ArrivalTime = datetime.now()

            postgreSQL_select_Query = "INSERT INTO userdata (lat, log, date, specific)VALUES (" + \
                str(latcor) + ", " + str(longcor) + ", '" + \
                str(ArrivalTime) + "', 'unknown')"

            cursor.execute(postgreSQL_select_Query)
            print()
            print("[SERVER] Data was added to the database")
            connection.commit()

        except (Exception, psycopg2.Error) as error:
            print("Error while fetching data from PostgreSQL", error)

        finally:
            # CLOSE CONNECTION
            if connection:
                cursor.close()
                connection.close()
                print("PostgreSQL connection is closed")

       # Get request
    if request.method == "GET":
        print()
        print("[SERVER] Server got pinged")
        return "Server is running"
    return "error"

    # Send Data Back


@ServerScript.route('/GetData', methods=['GET'])
def GetData():
    @after_this_request
    def add_header(response):
        response.headers.add('Access-Control-Allow-Origin', '*')
        return response

    # DB code

    try:
        connection = psycopg2.connect(user="NLB",
                                      password="selectedSections",
                                      host="localhost",
                                      port="55432",
                                      database="NightliveBerlin")
        cursor = connection.cursor()

        ArrivalTime = datetime.now()

        postgreSQL_select_Query = "SELECT lat, log, ((DATE_PART('day', '" + str(ArrivalTime) + "'::timestamp - date::timestamp) * 24) + (DATE_PART('hour', '" + str(ArrivalTime) + "'::timestamp - date::timestamp)) + (DATE_PART('minute', '" + str(ArrivalTime) + "'::timestamp - date::timestamp) / 60) + (DATE_PART('seconds', '" + str(
            ArrivalTime) + "'::timestamp - date::timestamp) / (60*60))) / 6 * 100 AS transparent, specific from userdata WHERE DATE_PART('hour', '" + str(ArrivalTime) + "'::timestamp - date::timestamp) < 6 AND DATE_PART('day', '" + str(ArrivalTime) + "'::timestamp - date::timestamp) = 0 AND DATE_PART('year', '" + str(ArrivalTime) + "'::timestamp - date::timestamp) = 0"

        cursor.execute(postgreSQL_select_Query)
        FetchedData = cursor.fetchall()

        coordinates = []
        transparency = []
        specific = []

        for row in FetchedData:

            Subcor = [row[0], row[1]]
            coordinates = coordinates + [Subcor]
            transparency = transparency + [row[2]]
            specific = specific + [row[3]]

        DataBaseJson = {
            "location": {
                "type": "MultiPoint",
                "coordinates": coordinates,
                "transparency": transparency,
                "specific": specific
            }
        }

    except (Exception, psycopg2.Error) as error:
        print("Error while fetching data from PostgreSQL", error)

    finally:
        # closing database connection.
        if connection:
            cursor.close()
            connection.close()
            print("PostgreSQL connection is closed")

    print()
    print("[SERVER] Data got sended to the client")

    return jsonify(DataBaseJson)


if __name__ == "__main__":
    ServerScript.run(host="localhost", port=1234)
