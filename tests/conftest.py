
from unittest.mock import MagicMock

import pytest

from dao.director import DirectorDAO
from dao.genre import GenreDAO
from dao.model.director import Director
from dao.model.genre import Genre
from dao.model.movie import Movie
from dao.movie import MovieDAO


@pytest.fixture()
def director_dao():
    director_dao = DirectorDAO(None)

    obj_1 = Director(id=1, name="Ivan Ivanov")
    obj_2 = Director(id=2, name="Petr Petrov")
    obj_3 = Director(id=3, name="Sidor Sidorov")

    director_dao.get_all = MagicMock(return_value=[obj_1, obj_2, obj_3])
    director_dao.get_one = MagicMock(return_value=obj_1)
    director_dao.update = MagicMock()
    director_dao.delete = MagicMock()
    director_dao.create = MagicMock(return_value=Director(id=3))

    return director_dao


@pytest.fixture()
def movie_dao():
    movie_dao = MovieDAO(None)

    obj_1 = Movie(
        id=1,
        title="1",
        description="1",
        trailer="1",
        year=2001,
        rating=9.1,
        genre_id=1,
        director_id=1,
    )
    obj_2 = Movie(
        id=2,
        title="2",
        description="2",
        trailer="2",
        year=2002,
        rating=8.1,
        genre_id=2,
        director_id=2,

    )

    movie_dao.get_all = MagicMock(return_value=[obj_1, obj_2])
    movie_dao.get_one = MagicMock(return_value=obj_1)
    movie_dao.update = MagicMock()
    movie_dao.delete = MagicMock()
    movie_dao.create = MagicMock(return_value=Movie(id=2))

    return movie_dao


@pytest.fixture()
def genre_dao():
    genre_dao = GenreDAO(None)

    obj_1 = Genre(id=1, name="Dich")
    obj_2 = Genre(id=2, name="Dich kakaya-to")

    genre_dao.get_all = MagicMock(return_value=[obj_1, obj_2])
    genre_dao.get_one = MagicMock(return_value=obj_1)
    genre_dao.update = MagicMock()
    genre_dao.delete = MagicMock()
    genre_dao.create = MagicMock(return_value=Genre(id=3))

    return genre_dao
