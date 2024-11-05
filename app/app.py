from flask import Flask, render_template, jsonify, request
import json
from flask_mail import Mail, Message
from flask_cors import CORS
import config

app = Flask(__name__)
cors = CORS(app)
mail = Mail(app)

app.config['MAIL_USE_SSL']=True
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = config.MAIL_USERNAME
app.config['MAIL_PASSWORD'] = config.MAIL_PASSWORD
app.config['MAIL_USE_TLS'] = False

mail = Mail(app)


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

    movie_title = movie["title"]
    movie_description = movie["overview"]

    first = 'https://image.tmdb.org/t/p/w1280'
    
    backdrop_path = first + movie.get("backdrop_path", "")
   
    #render template
    return render_template('trending_movie.html',
                           movie_title = movie_title,
                           movie_description= movie_description,
                           backdrop_path = backdrop_path)


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