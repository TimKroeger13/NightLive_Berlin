from flask import Flask, request, render_template

app = Flask(__name__)
app.debug = True


@app.route('/')
def index():
    return render_template('index.html')


# @app.route("/", methods=['GET', 'POST'])
# def index():
# if request.method == "POST":
##        name = int(request.form["name"])
##        name = name + 1
# return '%s' %name
# return render_template("index.html")


# if __name__ == "__main__":
# app.run()


if __name__ == "__main__":
    app.run()
