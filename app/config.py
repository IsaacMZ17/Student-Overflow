import os

class Config:
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL', 'postgresql+psycopg2://admin:admin123@127.0.0.1:5432/studentOverflow')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = os.getenv('SECRET_KEY', '4127705a6d2b380c7d0c8b5dd271482da29d')
    JWT_ALGORITHM = os.getenv('JWT_ALGORITHM', 'HS256')