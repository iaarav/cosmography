from flask import Flask, request, jsonify
import json

app = Flask(__name__)


@app.route('/get-json/')
def get_json_data():
    with open('data.json', mode="r") as file:
        data = json.load(file)
    return jsonify(data)


if __name__ == '__main__':
    app.run(debug=True)
