from unittest.mock import MagicMock

import pytest

from dao.director import DirectorDAO
from dao.model.director import Director
from service.director import DirectorService


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