from unittest.mock import MagicMock

import pytest

from service.genre import GenreService



class TestGenreService():
    @pytest.fixture(autouse=True)
    def genre_dao(self, genre_dao):
        self.genre_service = GenreService(dao=genre_dao)

    def test_get_one(self):
        genre = self.genre_service.get_one(1)
        assert genre is not None
        assert genre.id is not None

    def test_get_all(self):
        genre = self.genre_service.get_all()
        assert len(genre) > 0


    def test_create(self):
        genre_data = {"name": "Trash"}
        genre = self.genre_service.create(genre_data)
        assert genre.id is not None


    def test_update(self):
        genre_data = {"id": 2, "name": "Trash"}
        self.genre_service.update(genre_data)


    def delete(self):
        self.genre_service.delete(1)