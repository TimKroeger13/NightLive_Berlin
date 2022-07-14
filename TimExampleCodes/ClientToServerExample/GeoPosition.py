from operator import le
from flask import Flask, request, redirect, url_for, render_template, jsonify
import json


ServerScript = Flask(__name__)
ServerScript.debug = True


@ServerScript.route("/", methods=['GET', 'POST'])
def index():
    if request.method == "POST":
        print("testsignal, it WORKED!")
        data = request.form.getlist("NLBObject")

        JasonServerData = json.loads(data[0])
        print(JasonServerData["location"]["coordinates"])

        # create DB
        # ...

        # Send data back

        return "TESTMassage"
    if request.method == "GET":
        print("[SERVER] Server got pinged")
        return "Server is running"
    return "error"


if __name__ == "__main__":
    ServerScript.run(host="localhost", port=1234)
