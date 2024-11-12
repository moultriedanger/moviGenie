import sys
import os
import pytest


#Get project path
proj_path = os.path.abspath(os.getcwd()).split()[0]
app_path = os.path.join(proj_path, 'app')
sys.path.insert(0, app_path)
os.chdir(app_path)

from app import app

@pytest.fixture
def client():
 with app.test_client() as client:
    yield client

#test /landing valid
def test_landing_route(client):
 response = client.get('/landing')
 assert response.status_code == 200

#test /movies valid
def test_movie_route(client):
 response = client.get('/movies')
 assert response.status_code == 200
 print("working")

#test /trending_movie/<int:movie_id> valid 
def test_trending_movie_route(client):
    response = client.get('/trending_movie/933260')
    assert response.status_code == 200

#test /trending_movie/<int:movie_id> invalid - src chat gpt
def test_trending_movie_route_not_found(client):
    response = client.get('/trending_movie/999999999')  # Use a non-existent movie ID
    assert response.status_code == 404

#test /contact valid - src chat gpt
def test_contact_form(client):

    data = {
        "name": "John Doe",
        "email": "john@example.com",
        "comment": "This is a test message.",
        "honeypot": ""
    }
    response = client.post('/contact', json=data)
    assert response.status_code == 200