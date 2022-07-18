import psycopg2
import random
from datetime import datetime
import json
from flask import Flask, request, redirect, url_for, render_template, jsonify, after_this_request


def AddToDB():
    try:
        connection = psycopg2.connect(user="NLB",
                                      password="selectedSections",
                                      host="localhost",
                                      port="55432",
                                      database="NightliveBerlin")
        cursor = connection.cursor()

        postgreSQL_select_Query = "DELETE FROM userdata;"

        cursor.execute(postgreSQL_select_Query)
        connection.commit()

    except (Exception, psycopg2.Error) as error:
        print("Error while fetching data from PostgreSQL", error)

    finally:
        # CLOSE CONNECTION
        if connection:
            cursor.close()
            connection.close()
            print("PostgreSQL connection is closed")


AddToDB()
