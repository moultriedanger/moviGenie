from flask import Flask, jsonify
import json

from flask_cors import CORS
app = Flask(__name__)
cors = CORS(app)

@app.route('/hello')
def hello():
    return "Hello, World testing!"

@app.route('/movies')
def movies():

    with open('../www/data.json', 'r') as file:
        data = json.load(file)  # Load JSON data into a Python object
    
    return jsonify(data)  # Return the JSON response

if __name__ == '__main__':
    app.run(debug=True)