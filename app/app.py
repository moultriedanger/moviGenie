from flask import Flask, render_template, jsonify, request, redirect
import json
from flask_mail import Mail, Message 
from flask_cors import CORS
import config
import requests
from random import sample
import sqlite3
import os
import openai
# AIID = trainingAI.fine_tuned_model_id

app = Flask(__name__)
# app = Flask(__name__, template_folder='../templates')
CORS(app)
cors = CORS(app)
mail = Mail(app)

app.config['MAIL_USE_SSL']=True
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = config.MAIL_USERNAME
app.config['MAIL_PASSWORD'] = config.MAIL_PASSWORD
app.config['MAIL_USE_TLS'] = False

mail = Mail(app)

def create_app(test_config=False, shared_server=False):
    app = Flask(__name__)
    app.config['TESTING'] = test_config
    app.config['SHARED_SERVER'] = shared_server
    prepend = ''
    if app.config['SHARED_SERVER']:
        prepend = '/moviGenie'

    @app.route(prepend + '/landing')
    def landing():
        return render_template('landing.html')

    @app.route(prepend + '/process_genie_request', methods=['POST'])
    def process_genie_request():
        
        openai.api_key = config.GPT_API
        
        client = openai.OpenAI(api_key=config.GPT_API, timeout=40.0)
        
        with open("fine_tuned_model_id.json", "r") as f:
            data = json.load(f)
            fine_tuned_model_id = data["fine_tuned_model_id"]
        
        
        data = request.get_json()
        user_input = data.get('user_input')

        response = client.chat.completions.create(
            model=fine_tuned_model_id,  
            messages=[
                {"role": "system", "content": "You are a movie recommendation engine that only responds with relevant lists of movies (do NOT answer with TV shows) to valid requests for movies, any irrelevant questions are only to be met with the word INVALID."},
                {"role": "user", "content": user_input}
            ],
            max_tokens=150
        )

        gpt_response = response.choices[0].message.content
        
        # Split the GPT response into a list of movie titles
        movie_titles = gpt_response.split(',')
        movie_titles = [title.strip() for title in movie_titles]
        print(movie_titles)
        # Fetch movie details from TMDb for each movie title
        movie_details = []
        for title in movie_titles:
            movie_detail = fetch_movie_details_from_tmdb(title)
            if movie_detail:
                movie_details.append(movie_detail)
                
        # Return the movie details as a JSON response
        return jsonify({"movies": movie_details})

    def fetch_movie_details_from_tmdb(title):
        """Fetch movie details from TMDb API based on the movie title"""
        url = f'https://api.themoviedb.org/3/search/movie?query={title}&language=en-US'
        headers = {
            "accept": "application/json",
            "Authorization": f"Bearer {config.API_KEY}"
        }
        response = requests.get(url, headers=headers)
        
        if response.status_code != 200:
            print(f"Error fetching movie details for {title}: {response.status_code}")
            return None

        data = response.json()

        if data['results']:
            movie = data['results'][0]  # Get the first result (most relevant movie)
            return {
                "title": movie["title"],
                "overview": movie.get("overview", "No description available."),
                "poster_path": f'https://image.tmdb.org/t/p/w300{movie.get("poster_path", "")}',
                "movie_id": movie["id"]
            }
        
        return None

    @app.route(prepend + '/about')
    def about():
        return render_template('about.html')


    @app.route(prepend + '/movie')
    def movie():

        return render_template('movie.html')

    #Query movies for popular.js
    @app.route(prepend + '/movies')
    def movies():
    
        #open connection
        conn = sqlite3.connect(os.path.join(os.getcwd(), 'movieGenie.db'))
        cursor = conn.cursor()

        #create and execute quert
        query = "SELECT * FROM all_movies LIMIT 10"
        cursor.execute(query)
        results = cursor.fetchall()

        conn.close()

        #convert the query returned to json
        movies = []
        for row in results:
            movie = {
                'id': row[0],
                'title': row[1],
                'overview': row[2],
                'poster_path': row[3],
                'vote_average': row[4]
            }
            movies.append(movie)

        json_object = json.dumps(movies, indent=4)
        return json_object  


    @app.route(prepend + '/trending_movie/<int:movie_id>')
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

        # Fetch streaming platforms (for example, from TMDb API or JustWatch API)
        streaming_platforms = fetch_streaming_platforms(movie_id)
        for platform in streaming_platforms:
            print(platform['name'])
    
        #render template
        return render_template('trending_movie.html',
                            movie_title = movie_title, movie_id=movie_id,
                            movie_description= movie_description,
                            backdrop_path = backdrop_path, other_movies = other_movies, 
                            streaming_platforms=streaming_platforms)

    def fetch_streaming_platforms(movie_id):
        
        url = f'https://api.themoviedb.org/3/movie/{movie_id}/watch/providers'
        headers = {
            "accept": "application/json",
            "Authorization": f"Bearer {config.API_KEY}"
        }

        response = requests.get(url, headers=headers)
        data = response.json()

        # Extract streaming platforms from the response
        platforms = []
        seen_providers = set()  # Track provider names to avoid duplicates

        if 'results' in data:
            for country, provider_data in data['results'].items():
                keys = provider_data.keys()
                for key in keys:
                    if key == 'flatrate':
                        provider_info = provider_data.get(key)
                        for info in provider_info:
                            provider_name = info['provider_name']
                            if provider_name not in seen_providers:
                                platforms.append({
                                    'name': provider_name,
                                    'url': provider_data.get('link'),  # Example: link to the streaming platform
                                    'logo_url': f'https://www.themoviedb.org/t/p/w300{info["logo_path"]}'  # Example logo URL
                                })
                                seen_providers.add(provider_name)  # Mark as seen

        return platforms

    #('BR', {'link': 'https://www.themoviedb.org/movie/1087822-hellboy-the-crooked-man/watch?locale=BR', 'buy': [{'logo_path': '/9ghgSC0MA082EL6HLCW3GalykFD.jpg', 'provider_id': 2, 'provider_name': 'Apple TV', 'display_priority': 8}, {'logo_path': '/seGSXajazLMCKGB5hnRCidtjay1.jpg', 'provider_id': 10, 'provider_name': 'Amazon Video', 'display_priority': 13}, {'logo_path': '/8z7rC8uIDaTM91X0ZfkRf04ydj2.jpg', 'provider_id': 3, 'provider_name': 'Google Play Movies', 'display_priority': 14}], 'rent': [{'logo_path': '/9ghgSC0MA082EL6HLCW3GalykFD.jpg', 'provider_id': 2, 'provider_name': 'Apple TV', 'display_priority': 8}, {'logo_path': '/seGSXajazLMCKGB5hnRCidtjay1.jpg', 'provider_id': 10, 'provider_name': 'Amazon Video', 'display_priority': 13}, {'logo_path': '/8z7rC8uIDaTM91X0ZfkRf04ydj2.jpg', 'provider_id': 3, 'provider_name': 'Google Play Movies', 'display_priority': 14}]})


    @app.route(prepend + '/trending_movie/<int:movie_id>',methods=["POST"])
    @app.route(prepend +'/search/<int:movie_id>',methods=["POST"])
    def render_trailer(movie_id):
        url = f'https://api.themoviedb.org/3/movie/{movie_id}/videos'
        
        headers = {
            "accept": "application/json",
            "Authorization": f"Bearer {config.API_KEY}"
        }
        
        response = requests.get(url, headers=headers)

        if response.status_code != 200:
            
            return "Invalid request", 404

        videos = response.json()
        trailer = None
        teaser = None

        
        # First look for a trailer
        for video in videos.get("results", []):
            if video["type"] == "Trailer":
                trailer = video
                break
        
        # If no trailer look for a teaser
        if trailer:
            key = trailer['key']
            yurl = f"https://www.youtube.com/watch?v={key}"
            return jsonify({"url": yurl}) 
        else:
            for video in videos.get("results", []):
                if video["type"] == "Teaser":
                    teaser = video
                    break
            if teaser:
                key = teaser['key']
                yurl = f"https://www.youtube.com/watch?v={key}"
                return jsonify({"url": yurl})  
            else:
                return jsonify({"error": "Trailer not found"}), 400

    @app.route(prepend + '/search/<int:movie_id>')
    def render_search(movie_id):
    # make the same end point
        url = f"https://api.themoviedb.org/3/movie/{movie_id}?language=en-US"

        headers = {
            "accept": "application/json",
            "Authorization": f"Bearer {config.API_KEY}"
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
                            movie_id=movie_id,
                            movie_description= description,
                            backdrop_path = backdrop_path,
                            other_movies = movies)

    @app.route(prepend + '/random')
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
    

    @app.route(prepend +'/contact', methods=['POST'])
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