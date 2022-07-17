from flask import Flask, request, render_template, flash, jsonify
from flask_sqlalchemy import SQLAlchemy
import psycopg2
import os

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://flaskuser:flaskpassword@localhost/flaskdatabase'
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.secret_key = 'secret string'

db = SQLAlchemy(app)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == "POST":
        name = int(request.form["name"])
        name = name + 1
        #name = "done"
        return '%s' %name
    
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('SELECT * FROM latlontable;')
    books = cur.fetchall()
    cur.close()
    conn.close()
    return render_template('index.html', books = books)

def get_db_connection():
    conn = psycopg2.connect(host='localhost',
                            database='flaskdatabase',
                            user='flaskuser',
                            password='flaskpassword')
    return conn


#@app.route('/')
#def index():
#    conn = get_db_connection()
#    cur = conn.cursor()
#    cur.execute('SELECT * FROM latlontable;')
#    books = cur.fetchall()
#    cur.close()
#    conn.close()
#    return render_template('index.html', books=books)


# A function to add two numbers
@app.route("/add", methods=['POST'])
def add():
    a = request.form['a_value']
    b = request.form['b_value']
    #a = request.args.get('a')
    #b = request.args.get('b')
    #return jsonify({"result": a+b})
    return render_template("index.html")


##@app.route("/", methods=['GET', 'POST'])
##def index():
##    if request.method == "POST":
##        name = int(request.form["name"])
##        name = name + 1
##        return '%s' %name
##    return render_template("index.html")


##if __name__ == "__main__":
##    app.run()