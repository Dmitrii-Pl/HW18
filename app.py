from flask import Flask
from flask_restx import Api

from config import Config
from setup_db import db

# функция создания основного объекта app
from views.directors import director_ns
from views.genres import genre_ns
from views.movies import movie_ns


def create_app(config_object):
    application = Flask(__name__)
    application.config.from_object(config_object)
    register_extensions(application)
    return application


#
# функция подключения расширений (Flask-SQLAlchemy, Flask-RESTx, ...)
def register_extensions(application):
    db.init_app(application)
    api = Api(application)
    api.add_namespace(movie_ns)
    api.add_namespace(genre_ns)
    api.add_namespace(director_ns)


app = create_app(Config())

if __name__ == '__main__':
    app.run(debug=True)
