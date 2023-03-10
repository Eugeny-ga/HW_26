import pytest

from service.director import DirectorService


class TestDirectorService():
    @pytest.fixture(autouse=True)
    def director_dao(self, director_dao):
        self.director_service = DirectorService(dao=director_dao)

    def test_get_one(self):
        director = self.director_service.get_one(1)
        assert director is not None
        assert director.id is not None

    def test_get_all(self):
        directors = self.director_service.get_all()
        assert len(directors) > 0


    def test_create(self):
        director_data = {"name": "Imyarek"}
        director = self.director_service.create(director_data)
        assert director.id is not None


    def test_update(self):
        director_data = {"id": 2, "name": "Nikita"}
        self.director_service.update(director_data)


    def delete(self):
        self.director_service.delete(1)