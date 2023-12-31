from flask import Flask
from flask_migrate import Migrate
from flask_restx import Api

from config import Config
from setup_db import db
from views.directors import director_ns
from views.genres import genre_ns
from views.movies import movie_ns


def create_app(config_object):
    app = Flask(__name__)
    app.config.from_object(config_object)
    register_extensions(app)
    return app


def register_extensions(app):
    db.init_app(app)
    api = Api(app)
    api.add_namespace(movie_ns)
    api.add_namespace(director_ns)
    api.add_namespace(genre_ns)
    create_data(app, db)


def create_data(app, db):
    with app.app_context():
        db.create_all()


app = create_app(Config())
app.debug = True

migrate = Migrate(app, db, render_as_batch=True)

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8000, debug=True)
    # app.run(host="128.0.0.1", port=8000, debug=True)
