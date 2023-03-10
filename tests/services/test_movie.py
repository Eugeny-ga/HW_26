from unittest.mock import MagicMock

import pytest

from dao.model.movie import Movie
from dao.movie import MovieDAO
from service.movie import MovieService


@pytest.fixture()
def movie_dao():
    movie_dao = MovieDAO(None)

    obj_1 = Movie(
        id=1,
        title="1",
        description ="1",
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

class TestMovieService():
    @pytest.fixture(autouse=True)
    def movie_dao(self, movie_dao):
        self.movie_service = MovieService(dao=movie_dao)

    def test_get_all(self):
        movies = self.movie_service.get_all()
        assert len(movies) > 0

    def test_get_one(self):
        movie = self.movie_service.get_one(1)
        assert movie is not None
        assert movie.id is not None




    def test_create(self):
        movie_data = {
            "title": "3",
            "description": "3",
            "trailer": "3",
            "year": 2002,
            "rating": 8.1,
            "genre_id": 2,
            "director_id": 2
        }
        movie = self.movie_service.create(movie_data)
        assert movie.id is not None


    def test_update(self):
        movie_data = {"id": 2, "name": "Nikita"}
        self.movie_service.update(movie_data)


    def delete(self):
        self.movie_service.delete(1)