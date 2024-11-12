from flask import Flask, render_template, jsonify, request
import json
from flask_mail import Mail, Message 
from flask_cors import CORS
import config
from random import sample
app = Flask(__name__)
# app = Flask(__name__, template_folder='../templates')

cors = CORS(app)
mail = Mail(app)

app.config['MAIL_USE_SSL']=True
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = config.MAIL_USERNAME
app.config['MAIL_PASSWORD'] = config.MAIL_PASSWORD
app.config['MAIL_USE_TLS'] = False

mail = Mail(app)

@app.route('/landing')
def landing():
    return render_template('landing.html')


@app.route('/movies')
def movies():
    with open('../www/data.json', 'r') as file:
        data = json.load(file) 
    
    return jsonify(data)  

@app.route('/trending_movie/<int:movie_id>')
def make_movie_page(movie_id):

    #open the file
    with open('../www/data.json', 'r') as file:
        movies = json.load(file)

    movie = next((m for m in movies if m["id"] == movie_id), None)

    if movie is None:
        return "Movie not found", 404

    other_movies = [movie for movie in movies if movie["id"] != movie_id]
    
    # other_movie_posters = [movie["poster_path"] for movie in movies if movie["id"] != movie_id]


    movie_title = movie["title"]
    movie_description = movie["overview"]

    first = 'https://image.tmdb.org/t/p/w1280'
    
    backdrop_path = first + movie.get("backdrop_path", "")
   
    #render template
    return render_template('trending_movie.html',
                           movie_title = movie_title,
                           movie_description= movie_description,
                           backdrop_path = backdrop_path, other_movies = other_movies)

\


@app.route('/random')
def random():
    #open the file
    with open('../www/data.json', 'r') as file:
        movies = json.load(file)

    num_random_movies = 10
    one_random_movie = 1

    # generate one movie
    one_movie = sample(movies, one_random_movie)
    
    movie_title = one_movie[0]['title']
    movie_description = one_movie[0]["overview"]

    first = 'https://image.tmdb.org/t/p/w1280'
    
    backdrop_path = first + one_movie[0].get("backdrop_path", "")

    # generate three rows of random movies
    other_movies1 = sample(movies, num_random_movies)
    other_movies2 = sample(movies, num_random_movies)
    other_movies3 = sample(movies, num_random_movies)

    return render_template('random.html', movie_title = movie_title,
                           movie_description= movie_description, backdrop_path = backdrop_path,
                           one_movie = one_movie,
                           other_movies1 = other_movies1, other_movies2 = other_movies2, 
                           other_movies3 = other_movies3)




@app.route('/contact', methods=['POST'])
def contact_form():
     try:
         data = request.get_json()
         name = data.get("name")
         email = data.get("email")
         message = data.get("comment")
         honeypot = data.get('honeypot')
         if honeypot:
            return "error: Bot detected", 400
        
         msg = Message(subject="Contact Form Submission",
                       sender=app.config['MAIL_USERNAME'],
                       recipients=[config.MAIL_USERNAME]) 
         msg.body = f"Name: {name}\nEmail: {email}\nMessage: {message}"
         mail.send(msg)
         return "Email sent successfully", 200
    
     except Exception as e:
         return str(e), 500

if __name__ == '__main__':
    app.run(debug=True)