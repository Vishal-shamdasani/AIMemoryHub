from flask import Flask, send_file

app = Flask(__name__)

@app.route('/download-json', methods=['GET'])
def download_json():
    return send_file('data.json', mimetype='application/json', as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True)
