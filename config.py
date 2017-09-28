from os import path

# App details
BASE_DIRECTORY = path.abspath(path.dirname(__file__))
DEBUG = True
SECRET_KEY = 'keep_it_like_a_secret'

# Database details
SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://TerribleNews:Q5p7Ge!zucE*@TerribleNews.mysql.pythonanywhere-services.com/TerribleNews$deepquiz'
