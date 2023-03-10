import pytest

from service.director import DirectorService


class TestDirectorService:

    @pytest.fixture(autouse=True)
    def director_service(self, director_dao):
        self.director_service = DirectorService(dao=director_dao)

    def test_get_one(self):
        director = self.director_service.get_one(1)

        assert director is not None
        assert director.id == 1
        assert director.name == 'Director 1'

    def test_get_all(self):
        directors = self.director_service.get_all()

        assert directors is not None
        assert len(directors) > 1

    def test_create(self):
        director = {"name": "Director 3"}

        director_create = self.director_service.create(director)

        assert director_create is not None
        assert director_create.id is not None

    def test_update(self):
        director = {"name": "Director 3"}

        self.director_service.update(director)

    def test_delete(self):
        self.director_service.delete(3)
