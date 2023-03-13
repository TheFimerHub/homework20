import pytest

from service.movie import MovieService


class TestMovieService:
    @pytest.fixture(autouse=True)
    def movie_service(self, movie_fixture_dao):
        '''
        create a service movie for
        further use of the functions
        of services
        :param movie_dao:
        :return: None
        '''
        self.movie_service = MovieService(movie_fixture_dao)

    def test_get_all_movies(self):
        '''
        check the function get_all
        :return: None
        '''
        movie = self.movie_service.get_all()

        assert len(movie) > 0

    def test_get_one_movie(self):
        '''
        check the function get_one
        :return: None
        '''
        movie = self.movie_service.get_one(1)

        assert movie is not None
        assert movie.id is not None

    def test_create_movie(self):
        '''
        check the function create
        :return: None
        '''
        new_movie = {"name": "Capitan Marvel"}
        movie = self.movie_service.create(new_movie)

        assert movie is not None
        assert movie.id is not None

    def test_delete_movie(self):
        '''
        check dao function delete
        :return: None
        '''
        self.movie_service.delete(1)

    def test_update_movie(self):
        '''
        check dao function update
        :return: None
        '''
        new_movie = {"id": 3, "name": "Dream"}
        self.movie_service.update(new_movie)
