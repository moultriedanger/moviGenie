from flask import Flask, jsonify, request
import json
from flask_mail import Mail, Message
from flask_cors import CORS

app = Flask(__name__)
cors = CORS(app)
mail = Mail(app)

app.config['MAIL_USE_SSL']=True
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = 'MovieGenie4@gmail.com'
app.config['MAIL_PASSWORD'] = 'mmes ewxe hueo jtpe'
app.config['MAIL_USE_TLS'] = False

mail = Mail(app)


@app.route('/movies')
def movies():
    with open('../www/data.json', 'r') as file:
        data = json.load(file) 
    
    return jsonify(data)  

@app.route('/contact', methods=['POST'])
def contact_form():
    try:
        data = request.get_json()
        name = data.get("name")
        email = data.get("email")
        message = data.get("comment")

        msg = Message(subject="Contact Form Submission",
                      sender=app.config['MAIL_USERNAME'],
                      recipients=['MovieGenie4@gmail.com']) 
        msg.body = f"Name: {name}\nEmail: {email}\nMessage: {message}"
        mail.send(msg)
        return "Email sent successfully", 200
    
    except Exception as e:
        return str(e), 500

if __name__ == '__main__':
    app.run(debug=True)