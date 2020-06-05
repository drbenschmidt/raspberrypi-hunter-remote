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
    return "<h1>Distant Reading Archive</h1><p>This site is a prototype API for distant reading of science fiction novels.</p>"

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
    return jsonify(request.form)

app.run()