import pytest

from service.genre import GenreService


class TestGenreService:

    @pytest.fixture(autouse=True)
    def genre_service(self, genre_dao):
        self.genre_service = GenreService(dao=genre_dao)

    def test_get_one(self):
        genre = self.genre_service.get_one(2)

        assert genre is not None
        assert genre.id == 2
        assert genre.name == 'Genre 2'

    def test_get_all(self):
        genres = self.genre_service.get_all()

        assert genres is not None
        assert len(genres) > 1

    def test_create(self):
        genre = {"name": "Genre 3"}

        genre_create = self.genre_service.create(genre)

        assert genre_create is not None
        assert genre_create.id is not None

    def test_update(self):
        genre = {"name": "Genre 3"}

        self.genre_service.update(genre)

    def test_delete(self):
        self.genre_service.delete(3)
