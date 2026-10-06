import os
from dotenv import load_dotenv

load_dotenv(os.path.join(os.path.dirname(os.path.dirname(__file__)), '.env'))


class Config:
    SECRET_KEY = os.getenv('SECRET_KEY', 'dev-secret-key')
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL', 'postgresql://postgres:postgres@localhost:5432/learn_vocabulary')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    CORS_ORIGINS = [os.getenv('FRONTEND_URL', 'http://localhost:5173')]
