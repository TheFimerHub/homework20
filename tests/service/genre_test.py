import pytest

from service.genre import GenreService


class TestGenreService:
    @pytest.fixture(autouse=True)
    def genre_service(self, genre_fixture_dao):
        '''
        create a service genre for
        further use of the functions
        of services
        :param genre_dao:
        :return: None
        '''
        self.genre_service = GenreService(genre_fixture_dao)

    def test_get_all_genres(self):
        '''
        check the function get_all
        :return: None
        '''
        genre = self.genre_service.get_all()

        assert len(genre) > 0

    def test_get_one_genre(self):
        '''
        check the function get_one
        :return: None
        '''
        genre = self.genre_service.get_one(1)

        assert genre is not None
        assert genre.id is not None

    def test_create_genre(self):
        '''
        check the function create
        :return: None
        '''
        new_genre = {"name": "comedy"}
        genre = self.genre_service.create(new_genre)

        assert genre is not None
        assert genre.id is not None

    def test_delete_genre(self):
        '''
        check dao function delete
        :return: None
        '''
        self.genre_service.delete(1)

    def test_update_genre(self):
        '''
        check dao function update
        :return: None
        '''
        new_genre = {"id": 3, "name": "action"}
        self.genre_service.update(new_genre)
