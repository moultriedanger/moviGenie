from flask import Flask, jsonify, render_template
import json

from flask_cors import CORS
app = Flask(__name__)
app = Flask(__name__, template_folder='../templates')

cors = CORS(app)
# http://127.0.0.1/landing

@app.route('/landing')
def landing():
    return render_template('landing.html')

@app.route('/lan')
def lan():
    return render_template('lan.html')

@app.route('/movies')
def movies():

    with open('../www/data.json', 'r') as file:
        data = json.load(file)  # Load JSON data into a Python object
    
    return jsonify(data)   # Return the JSON response

@app.route('/movies/<int:movie_id>')
def get_movie(movie_id):
    with open('../www/data.json', 'r') as file:
        data = json.load(file)  # Load JSON data into a Python object

    # Find the movie by ID
    movie = next((movie for movie in data if movie['id'] == movie_id), None)
    
    if movie:
        return jsonify(movie)  # Return the JSON response for the specific movie
    else:
        return jsonify({'error': 'Movie not found'}), 404  # Return an error if movie not found


if __name__ == '__main__':
    app.run(debug=True)