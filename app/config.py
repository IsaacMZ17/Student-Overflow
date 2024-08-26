import os

class Config:
    SQLALCHEMY_DATABASE_URI ='postgresql+psycopg2://user:password@localhost:port/database'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = ''
    JWT_ALGORITHM = 'HS256'
