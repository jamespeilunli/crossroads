from flask import Flask, jsonify, render_template, request
from lib.crossroads import Crossroads

app = Flask(__name__)

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
    crossroads = Crossroads()
    models_list = crossroads.list_models()

    return jsonify({"result": models_list})

if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)

