from flask import Flask, jsonify, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/get_response', methods=["POST"])
def process_array():
    data = request.get_json()
    messages = data["messages"]
    return jsonify({"result": messages})

if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)

