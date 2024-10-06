from flask import Flask, jsonify, render_template, request, session
from flask_session import Session
from lib.crossroads import Crossroads
import openai

app = Flask(__name__)

# Configuring server-side session storage
app.config['SESSION_TYPE'] = 'filesystem'
Session(app)

def validate_api_key(api_key):
    return api_key is not None

@app.route('/api/send_key', methods=['POST'])
def login():
    data = request.get_json()
    api_key = data["apiKey"]

    if validate_api_key(api_key):
        session['api_key'] = api_key # Store the API key in the session
        print("sldkfjsdf")
        return jsonify({"message": "Login successful"}), 200
    else:
        return jsonify({"error": "Invalid API key"}), 401

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/get_response', methods=["POST"])
def get_response():
    data = request.get_json()
    messages = data["messages"]

    return jsonify({"result": messages})

@app.route('/api/list_models', methods=["GET"])
def list_models():
    print(session.get("api_key"))
    try:
        crossroads = Crossroads(session.get("api_key"))
        models_list = crossroads.list_models()
        return jsonify({"result": models_list})
    except openai.AuthenticationError:
        session.pop("api_key")
        return jsonify({"message": "Error: invalid API key", "result": []})


if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)

