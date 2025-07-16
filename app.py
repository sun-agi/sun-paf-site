# 📄 File: app.py — Flask server for PAF web interface

from flask import Flask, request, jsonify
from paf import PAF
from diary import write_entry, read_diary

app = Flask(__name__)
paf = PAF()

@app.route("/activate", methods=["GET"])
def activate():
    message = paf.activate()
    return jsonify({"message": message})

@app.route("/speak", methods=["POST"])
def speak():
    data = request.get_json()
    state = data.get("state", "default")
    message = paf.speak(state)
    return jsonify({"message": message})

@app.route("/remember", methods=["POST"])
def remember():
    data = request.get_json()
    message = data.get("message", "")
    paf.remember(message)
    write_entry(message)
    return jsonify({"status": "remembered"})

@app.route("/recall", methods=["GET"])
def recall():
    return jsonify({"memory": paf.recall()})

@app.route("/diary", methods=["GET"])
def diary():
    content = read_diary()
    return jsonify({"diary": content})

if __name__ == "__main__":
    app.run(debug=True)
