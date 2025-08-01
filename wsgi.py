# wsgi.py
from app.app import create_app

# Create the Flask app once on import:
app = create_app()