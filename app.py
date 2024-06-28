from flask import Flask, request, jsonify
import json

app = Flask(__name__)


@app.route('/get-json/')
def get_json_data():
    with open('data.json', mode="r") as file:
        data = json.load(file)

    return jsonify(data)


@app.route('/add-json-data/', methods=['POST'])
def add_data():
    new_data = request.get_json()
    print("Received data:", new_data)  # Debug statement

    try:
        with open('data.json', mode="r") as file:
            data = json.load(file)
        print("Current data in file:", data)  # Debug statement
    except json.JSONDecodeError as e:
        print("Error reading JSON file:", e)
        data = []

    data.append(new_data)
    print("Updated data:", data)  # Debug statement

    with open('data.json', mode="w") as file:
        json.dump(data, file, indent=4)

    return jsonify(new_data), 201


if __name__ == '__main__':
    app.run(debug=True)
