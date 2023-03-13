import pytest

from service.director import DirectorService

class TestDirectorService:
    @pytest.fixture(autouse=True)
    def director_service(self, director_fixture_dao):
        '''
        create a service director for
        further use of the functions
        of services
        :param director_dao:
        :return: None
        '''
        self.director_service = DirectorService(director_fixture_dao)

    def test_get_all_directors(self):
        '''
        check the function get_all
        :return: None
        '''
        director = self.director_service.get_all()

        assert len(director) > 0

    def test_get_one_director(self):
        '''
        check the function get_one
        :return: None
        '''
        director = self.director_service.get_one(1)

        assert director is not None
        assert director.id is not None

    def test_create_director(self):
        '''
        check the function create
        :return: None
        '''
        new_director = {"name": "Masha"}
        director = self.director_service.create(new_director)

        assert director is not None
        assert director.id is not None

    def test_delete_director(self):
        '''
        check dao function delete
        :return: None
        '''
        self.director_service.delete(1)

    def test_update_director(self):
        '''
        check dao function update
        :return: None
        '''
        new_director = {"id": 3, "name": "Nikita"}
        self.director_service.update(new_director)