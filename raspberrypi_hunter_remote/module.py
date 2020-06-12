import flask
from flask import request, jsonify

app = flask.Flask(__name__)
app.config["DEBUG"] = True

# [GET] / => home
# [GET] /fans => list fan ids
# [GET] /fans/{id} => get fan info
# [PATCH] /fans/{id} => set values

local_fans = [
    {
        "id": 1,
        "name": "Downstairs Fan"
    }, {
        "id": 2,
        "name": "Bedroom Fan"
    }
]

@app.route('/', methods=['GET'])
def home():
    return "<h1>raspberrypi-hunter-remote</h1><p>Remember to modify your fans.py!</p>"

@app.route('/fans', methods=['GET'])
def fans():
    return jsonify(local_fans)

@app.route('/fans/<int:id>', methods=['GET'])
def fans_id(id):
    results = []

    for fan in local_fans:
        if (fan['id'] == id):
            results.append(fan)

    # Use the jsonify function from Flask to convert our list of
    # Python dictionaries to the JSON format.
    return jsonify(results)

@app.route('/fans/<int:id>', methods=['PATCH'])
def fans_id_patch(id):
    request_data = request.json

    print(request_data)

    # TODO: Validate Request

    if "speed" in request_data:
        print(f"Setting fan({id}) speed to {request_data['speed']}")

    if "lightToggle" in request_data:
        print(f"Setting fan({id}) light toggle to {request_data['lightToggle']}")

    return jsonify({ "success": True })

app.run(host='0.0.0.0', port='8083')