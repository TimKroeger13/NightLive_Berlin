import psycopg2
import random
from datetime import datetime
import json
from flask import Flask, request, redirect, url_for, render_template, jsonify, after_this_request

# Add data to the database


try:
    connection = psycopg2.connect(user="NLB",
                                  password="selectedSections",
                                  host="localhost",
                                  port="55432",
                                  database="NightliveBerlin")
    cursor = connection.cursor()

    # TEMPORARY add generated data

    for x in range(10):

        ExLat = 52.5101148
        ExLong = 13.3303686

        Newlat = ExLat + random.uniform(-1, 1)
        NewLong = ExLong + random.uniform(-1, 1)

        # Add Data to the database

        ArrivalTime = datetime.now()

        postgreSQL_select_Query = "INSERT INTO userdata (lat, log, date, specific)VALUES (" + \
            str(Newlat) + ", " + str(NewLong) + ", '" + \
            str(ArrivalTime) + "', 'unknown')"

        cursor.execute(postgreSQL_select_Query)
        print()
        print("[SERVER] Random Data was added")
        connection.commit()


except (Exception, psycopg2.Error) as error:
    print("Error while fetching data from PostgreSQL", error)

finally:
    # CLOSE CONNECTION
    if connection:
        cursor.close()
        connection.close()
        print("PostgreSQL connection is closed")
