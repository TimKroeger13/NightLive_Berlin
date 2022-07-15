import psycopg2
import random
from datetime import datetime


# Add data to the database

def AddToDB():
    try:
        connection = psycopg2.connect(user="NLB",
                                      password="selectedSections",
                                      host="localhost",
                                      port="55432",
                                      database="NightliveBerlin")
        cursor = connection.cursor()

        # TEMPORARY add generated data

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
        print("Selecting rows from mobile table using cursor.fetchall")
        connection.commit()

    except (Exception, psycopg2.Error) as error:
        print("Error while fetching data from PostgreSQL", error)

    finally:
        # CLOSE CONNECTION
        if connection:
            cursor.close()
            connection.close()
            print("PostgreSQL connection is closed")


def GetDB():

    try:
        connection = psycopg2.connect(user="NLB",
                                      password="selectedSections",
                                      host="localhost",
                                      port="55432",
                                      database="NightliveBerlin")
        cursor = connection.cursor()
        #postgreSQL_select_Query = "select * from userdata"

        ArrivalTime = datetime.now()

        postgreSQL_select_Query = "SELECT lat, log, ((DATE_PART('day', '" + str(ArrivalTime) + "'::timestamp - date::timestamp) * 24) + (DATE_PART('hour', '" + str(ArrivalTime) + "'::timestamp - date::timestamp)) + (DATE_PART('minute', '" + str(ArrivalTime) + "'::timestamp - date::timestamp) / 60) + (DATE_PART('seconds', '" + str(
            ArrivalTime) + "'::timestamp - date::timestamp) / (60*60))) / 6 * 100 AS transparent, specific from userdata WHERE DATE_PART('hour', '" + str(ArrivalTime) + "'::timestamp - date::timestamp) < 6 AND DATE_PART('day', '" + str(ArrivalTime) + "'::timestamp - date::timestamp) = 0"

        cursor.execute(postgreSQL_select_Query)
        mobile_records = cursor.fetchall()

        print(mobile_records)

    except (Exception, psycopg2.Error) as error:
        print("Error while fetching data from PostgreSQL", error)

    finally:
        # closing database connection.
        if connection:
            cursor.close()
            connection.close()
            print("PostgreSQL connection is closed")


GetDB()
