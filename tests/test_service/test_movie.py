import pytest

from service.movie import MovieService


class TestMovieService:

    @pytest.fixture(autouse=True)
    def movie_service(self, movie_dao):
        self.movie_service = MovieService(dao=movie_dao)

    def test_get_one(self):
        movie = self.movie_service.get_one(1)

        assert movie is not None
        assert movie.id == 1
        assert movie.title == 'Movie 1 Title'

    def test_get_all(self):
        movies = self.movie_service.get_all()

        assert movies is not None
        assert len(movies) > 1

    def test_create(self):
        movie = {
            "title": 'Movie 3 Title', "description": 'Descr 3', "trailer": 'link.to/movie3_trailer',
            "year": 2023, "rating": 7.7, "genre_id": 3, "director_id": 6
        }

        movie_create = self.movie_service.create(movie)

        assert movie_create is not None
        assert movie_create.id is not None

    def test_update(self):
        movie = {
            "id": 3, "title": 'Movie 3 Title', "description": 'Descr 3 new', "trailer": 'link.to/movie3_trailer_new',
            "year": 2019, "rating": 6.6, "genre_id": 3, "director_id": 6
        }

        self.movie_service.update(movie)

    def test_delete(self):
        self.movie_service.delete(3)
