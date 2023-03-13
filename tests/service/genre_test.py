import pytest

from service.genre import GenreService


class TestGenreService:
    @pytest.fixture(autouse=True)
    def genre_service(self, genre_dao):
        '''

        :param genre_dao:
        :return: None
        '''
        self.genre_service = GenreService(genre_dao)

    def test_get_all_genres(self):
        genre = self.genre_service.get_all()

        assert len(genre) > 0

    def test_get_one_genre(self):
        genre = self.genre_service.get_one(1)

        assert genre is not None
        assert genre.id is not None

    def test_create(self):
        new_genre = {"name": "comedy"}
        genre = self.genre_service.create(new_genre)

        assert genre is not None
        assert genre.id is not None

    def test_delete(self):
        self.genre_service.delete(1)

    def test_update(self):
        new_genre = {"id": 3, "name": "action"}
        self.genre_service.update(new_genre)
