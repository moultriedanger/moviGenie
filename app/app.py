from flask import Flask, render_template, jsonify, request
import json
from flask_mail import Mail, Message 
from flask_cors import CORS
import config
import requests
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

@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/movie')
def movie():
    return render_template('movie.html')

#Displays movies onto movie.html
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

    #Search for movie data associated with desired id
    movie = next((m for m in movies if m["id"] == movie_id), None)

    #throw error if id invalid
    if movie is None:
        return "Movie not found", 404

    other_movies = [movie for movie in movies if movie["id"] != movie_id]
    
    # other_movie_posters = [movie["poster_path"] for movie in movies if movie["id"] != movie_id]

    movie_title = movie["title"]
    movie_description = movie["overview"]

    #create poster path
    first = 'https://image.tmdb.org/t/p/w1280'
    backdrop_path = first + movie.get("backdrop_path", "")
   
    #render template
    return render_template('trending_movie.html',
                           movie_title = movie_title,
                           movie_description= movie_description,
                           backdrop_path = backdrop_path, other_movies = other_movies)

@app.route('/search/<int:movie_id>')
def render_search(movie_id):

    url = f"https://api.themoviedb.org/3/movie/{movie_id}?language=en-US"

    headers = {
        "accept": "application/json",
        "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiJlNjJkNzBkYTg0MWQyMWQ1ZDc1ZGQ3NGUyYjlkNmNiZiIsIm5iZiI6MTczMDgzNjcyMi4xNjY4MTk2LCJzdWIiOiI2NmQyMGVkYWIyNzBiY2I5ZmNhN2YxODQiLCJzY29wZXMiOlsiYXBpX3JlYWQiXSwidmVyc2lvbiI6MX0.0c4p-RZjSKxI21xOLPoztE0bETGYcLxjtVAySQpNS9E"
    }
    response = requests.get(url, headers=headers)

    #Null check movie
    if not response:
        return "Invalid request", 404

    movie = response.json()

    title = movie.get("title", "Title not found") 
    description = movie.get("overview", "Title not found") 

    first = 'https://image.tmdb.org/t/p/w1280'
    backdrop_path = first + movie.get("backdrop_path", "")

    # load other movies
    with open('../www/data.json', 'r') as file:
        movies = json.load(file)

    #null check movies
    if not movies:
        return jsonify({"error": "Related movies not found"}), 400

    return render_template('trending_movie.html',
                           movie_title = title,
                           movie_description= description,
                           backdrop_path = backdrop_path,
                           other_movies = movies)

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