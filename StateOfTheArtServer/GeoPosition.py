from operator import le
from flask import Flask, request, redirect, url_for, render_template, jsonify, after_this_request
import json


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

        # create DB
        # ...

        # Send data back

        # Some Manipulation

        JasonServerData["location"]["coordinates"][0] = JasonServerData["location"]["coordinates"][0] + 1
        JasonServerData["location"]["coordinates"][1] = JasonServerData["location"]["coordinates"][1] + 1

        # Jason to String
        ClientJason = json.dumps(JasonServerData)

        print(ClientJason)
        print(type(ClientJason))

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

    jsonResp = {
        "location": {
            "type": "MultiPoint",
            "coordinates": [
                [
                    52.5739526,
                    13.4118061
                ],
                [
                    52.6739526,
                    13.3118061
                ],
                [
                    52.3739526,
                    13.2218061
                ],
                [
                    52.8639526,
                    13.1218061
                ],
                [
                    52.8539526,
                    13.6118061
                ]
            ],
            "transparency": [
                20,
                4,
                7,
                50,
                4
            ],
            "specific": [
                "unknown",
                "unknown",
                "unknown",
                "unknown",
                "unknown"
            ]
        }
    }

    print()
    print("[SERVER] Data got sended to the client")

    return jsonify(jsonResp)


if __name__ == "__main__":
    ServerScript.run(host="localhost", port=1234)
