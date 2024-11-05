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

def test_some_route(client):
 response = client.get('/movies')
 print("Success: Status code is 200.")
 assert response.status_code == 200