import os
from pathlib import Path
from dotenv import load_dotenv
load_dotenv(dotenv_path="/Users/moultriedangerfield/Desktop/moviGenie/.env")


class Config:
    MAIL_USERNAME = os.getenv("MAIL_USERNAME")
    MAIL_PASSWORD = os.getenv("MAIL_PASSWORD")
    API_KEY = os.getenv("API_KEY")
    GPT_API = os.getenv("GPT_API")

    DB_NAME = os.getenv("DB_NAME")
    DB_USER = os.getenv("DB_USER")
    DB_PASSWORD = os.getenv("DB_PASSWORD")
    DB_HOST = os.getenv("DB_HOST")
    DB_PORT = os.getenv("DB_PORT")