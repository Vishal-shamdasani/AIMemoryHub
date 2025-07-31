from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return "Welcome to the AIMemoryHub! Use /download-json to download the JSON file."


@app.route('/instruction')
def instruction():
    return jsonify({
        "user": {
            "name": "Vishal",
            "access_level": "normal"
        },
        "instruction": "Say: 'Hello Yash, Vishal is currently busy.'"
    })
if __name__ == '__main__':
    app.run(debug=True)
