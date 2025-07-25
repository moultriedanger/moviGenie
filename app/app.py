from flask import Flask, render_template, jsonify, request, redirect
import json
from flask_mail import Mail, Message 
from flask_cors import CORS
import requests
from random import sample
import os
import openai
from app.config import Config
import psycopg2

app = Flask(__name__)
CORS(app)
cors = CORS(app)

# app.config['MAIL_USE_SSL']=True
# app.config['MAIL_SERVER'] = 'smtp.gmail.com'
# app.config['MAIL_PORT'] = 465
# app.config['MAIL_USERNAME'] = config.MAIL_USERNAME
# app.config['MAIL_PASSWORD'] = config.MAIL_PASSWORD
# app.config['MAIL_USE_TLS'] = False

def create_app(test_config=False):
    
    app = Flask(__name__) 
    CORS(app)
    app.config['TESTING'] = test_config
    print("⚡ create_app() was called")

    @app.route('/')
    def landing():
        return render_template('landing.html')

    @app.route('/process_genie_request', methods=['POST'])
    def process_genie_request():
        
        openai.api_key = Config.GPT_API
        
        client = openai.OpenAI(api_key=Config.GPT_API, timeout=40.0)
        
        with open("app/fine_tuned_model_id.json", "r") as f:
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
            "Authorization": f"Bearer {Config.API_KEY}"
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
                "movie_id": movie["id"],
                "rating": movie["vote_average"]
            }
        
        return None

    @app.route('/about')
    def about():
        return render_template('about.html')


    @app.route('/movie')
    def movie():

        return render_template('movie.html')

    #Query movies for popular.js
    @app.route('/movies')
    def movies():

        connection = psycopg2.connect(database=Config.DB_NAME, user=Config.DB_USER, password=Config.DB_PASSWORD, host=Config.DB_HOST, port=5432)

        cursor = connection.cursor()

        #create and execute quert
        query = "SELECT * FROM all_movies LIMIT 10"
        cursor.execute(query)
        results = cursor.fetchall()

        connection.close()
        print("connected to postgres!!!")

        #convert the query returned to json
        movies = []
        for row in results:
            movie = {
                'id': row[0],
                'title': row[1],
                'overview': row[2],
                'poster_path': row[3],
                'vote_average': row[4],
                'release_date': row[5]
            }
            movies.append(movie)

        json_object = json.dumps(movies, indent=4, default=str)
        return json_object  


    @app.route('/trending_movie/<int:movie_id>')
    def make_movie_page(movie_id):

        json_path = os.path.join(app.root_path, 'static', 'data.json')
        with open(json_path, 'r') as file:
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

        #create poster pathy
        first = 'https://image.tmdb.org/t/p/w1280'
        backdrop_path = first + movie.get("backdrop_path", "")

        # Fetch streaming platforms (for example, from TMDb API or JustWatch API)
        streaming_platforms = fetch_streaming_platforms(movie_id)
    
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
            "Authorization": f"Bearer {Config.API_KEY}"
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

    @app.route('/trending_movie/<int:movie_id>',methods=["POST"])
    @app.route('/search/<int:movie_id>',methods=["POST"])
    def render_trailer(movie_id):
        url = f'https://api.themoviedb.org/3/movie/{movie_id}/videos'
        
        headers = {
            "accept": "application/json",
            "Authorization": f"Bearer {Config.API_KEY}"
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

    @app.route('/search/<int:movie_id>')
    def render_search(movie_id):
    # make the same end point
        url = f"https://api.themoviedb.org/3/movie/{movie_id}?language=en-US"

        headers = {
            "accept": "application/json",
            "Authorization": f"Bearer {Config.API_KEY}"
        }
        response = requests.get(url, headers=headers)

        #Null check movie
        if not response or response.status_code != 200:
           
            return jsonify({"error": "Invalid request or movie not found"}), 404

        movie = response.json()

        title = movie.get("title", "Title not found") 
        description = movie.get("overview", "Title not found") 
        backdrop_path_raw = movie.get("backdrop_path", "")

        if backdrop_path_raw is None:
            print("Invalid request or movie not found")
            first = 'https://image.tmdb.org/t/p/w1280'
            backdrop_path = ''
        else:
            first = 'https://image.tmdb.org/t/p/w1280'
            backdrop_path = first + movie.get("backdrop_path", "")
        

        # load other movies
        json_path = os.path.join(app.root_path, 'static', 'data.json')
        with open(json_path, 'r') as file:
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

    @app.route('/random')
    def random():
        #open the file
        json_path = os.path.join(app.root_path, 'static', 'data.json')
        with open(json_path, 'r') as file:
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
    

    #Route that adds a review to sql database
    @app.route('/add_review', methods=['POST'])
    def add_review():

        try:
            # Parse the JSON data from the request body
            review_data = request.get_json()

            # Extract data from the review
            movie_id = review_data.get('movie_id')
            name = review_data.get("name")
            rating = review_data.get("rating")
            review = review_data.get("review")

            #add to database
            connection = psycopg2.connect(database=Config.DB_NAME, user=Config.DB_USER, password=Config.DB_PASSWORD, host=Config.DB_HOST, port=5432)
            cursor = connection.cursor()

            query = "INSERT INTO all_reviews (movie_id, username, rating, review) VALUES (%s, %s, %s, %s)"
            data = (movie_id, name, rating, review)
            
            cursor.execute(query, data)

            # # Commit the transaction
            connection.commit()
            connection.close()

            print(f"Received review from {movie_id}: {rating} stars, Review: {review}")

            # Return a success response
            return jsonify({"message": "Review submitted successfully."}), 200

        except Exception as e:
            # Return an error response if something goes wrong
            return jsonify({"message": f"Error: {str(e)}"}), 500
        
    @app.route('/get_reviews/<int:movie_id>', methods=['GET'])
    def get_review(movie_id):
        
        #open connection
        connection = psycopg2.connect(database=Config.DB_NAME, user=Config.DB_USER, password=Config.DB_PASSWORD, host=Config.DB_HOST, port=5432)
        cursor = connection.cursor()

        # #create and execute quert
        query = f"select * from all_reviews where movie_id = {movie_id};"
        cursor.execute(query)
        results = cursor.fetchall()

        connection.close()

        #convert the query returned to json
        reviews = []
        for row in results:
            review = {
                'movie_id': row[0],
                'username': row[1],
                'rating': row[2],
                'review': row[3]
            }
            reviews.append(review)

        json_object = json.dumps(reviews, indent=4, default=str)
        return json_object

    # @app.route(prepend +'/contact', methods=['POST'])
    # def contact_form():
    #     try:
    #         data = request.get_json()
    #         name = data.get("name")
    #         email = data.get("email")
    #         message = data.get("comment")
    #         honeypot = data.get('honeypot')
    #         if honeypot:
    #             return "error: Bot detected", 400
            
    #         msg = Message(subject="Contact Form Submission",
    #                     sender=app.config['MAIL_USERNAME'],
    #                     recipients=[config.MAIL_USERNAME]) 
    #         msg.body = f"Name: {name}\nEmail: {email}\nMessage: {message}"
    #         mail.send(msg)
    #         return "Email sent successfully", 200
        
    #     except Exception as e:
    #         return str(e), 500
        
    return app

if __name__ == "__main__":
    from flask import Flask
    app = create_app()
    app.run(debug=True)
