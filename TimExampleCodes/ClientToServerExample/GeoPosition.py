from operator import le
from flask import Flask, request, redirect, url_for, render_template, jsonify


ServerScript = Flask(__name__)
ServerScript.debug = True


@ServerScript.route("/", methods=['GET', 'POST'])
def index():
    if request.method == "POST":
        print("testsignal, it WORKED!")
        data = request.form
        print("Message:", data)
        return "TESTMassage"
    if request.method == "GET":
        print("This is a GET request")
        return "testGET"
    return "something different happend"


if __name__ == "__main__":
    ServerScript.run(host="localhost", port=1234)
