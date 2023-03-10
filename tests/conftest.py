import pytest
from unittest.mock import MagicMock

from dao.model.movie import Movie
from dao.movie import MovieDAO

from dao.model.director import Director
from dao.director import DirectorDAO

from dao.model.genre import Genre
from dao.genre import GenreDAO


@pytest.fixture
def movie_dao():
    movie_dao = MovieDAO(None)

    movie1 = Movie(id=1, title='Movie 1 Title', description='Descr 1', trailer='link.to/movie1_trailer',
                   year=2021, rating=5.5, genre_id=1, director_id=2)
    movie2 = Movie(id=2, title='Movie 2 Title', description='Descr 2', trailer='link.to/movie2_trailer',
                   year=2022, rating=6.0, genre_id=2, director_id=4)
    movie3 = Movie(id=3, title='Movie 3 Title', description='Descr 3', trailer='link.to/movie3_trailer',
                   year=2023, rating=7.7, genre_id=3, director_id=6)

    movie_dao.get_one = MagicMock(return_value=movie1)
    movie_dao.get_all = MagicMock(return_value=[movie1, movie2, movie3])
    movie_dao.create = MagicMock(return_value=Movie(id=3))
    movie_dao.update = MagicMock()
    movie_dao.delete = MagicMock()

    return movie_dao


@pytest.fixture
def director_dao():
    director_dao = DirectorDAO(None)

    director1 = Director(id=1, name='Director 1')
    director2 = Director(id=2, name='Director 2')
    director3 = Director(id=3, name='Director 3')

    director_dao.get_one = MagicMock(return_value=director1)
    director_dao.get_all = MagicMock(return_value=[director1, director2, director3])
    director_dao.create = MagicMock(return_value=Director(id=3))
    director_dao.update = MagicMock()
    director_dao.delete = MagicMock()

    return director_dao


@pytest.fixture
def genre_dao():
    genre_dao = GenreDAO(None)

    genre1 = Genre(id=1, name='Genre 1')
    genre2 = Genre(id=2, name='Genre 2')
    genre3 = Genre(id=3, name='Genre 3')

    genre_dao.get_one = MagicMock(return_value=genre2)
    genre_dao.get_all = MagicMock(return_value=[genre1, genre2, genre3])
    genre_dao.create = MagicMock(return_value=Genre(id=3))
    genre_dao.update = MagicMock()
    genre_dao.delete = MagicMock()

    return genre_dao
