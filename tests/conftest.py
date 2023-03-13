from unittest.mock import MagicMock

import pytest

from dao.director import DirectorDAO
from dao.genre import GenreDAO
from dao.model.director import Director
from dao.model.genre import Genre
from dao.model.movie import Movie
from dao.movie import MovieDAO


@pytest.fixture
def director_fixture_dao():
    '''
    We will create a fixture with a mock,
    and here we have 3 instances of the class.
    :return: values for each method in directorDAO
    '''
    director_dao = DirectorDAO(None)

    misha = Director(id=1, name='Misha')
    pasha = Director(id=2, name='Pasha')
    egor = Director(id=3, name='Egor')

    director_dao.get_one = MagicMock(return_value=misha)
    director_dao.get_all = MagicMock(return_value=[misha, pasha, egor])
    director_dao.create = MagicMock(return_value=Director(id=3))
    director_dao.update = MagicMock()
    director_dao.delete = MagicMock()

    return director_dao


@pytest.fixture
def genre_fixture_dao():
    '''
    We will create a fixture with a mock,
    and here we have 3 instances of the class.
    :return: values for each method in GenreDAO
    '''
    genre_dao = GenreDAO(None)

    thriller = Genre(id=1, name='thriller')
    drama = Genre(id=2, name='drama')
    horror = Genre(id=3, name='horror')

    genre_dao.get_one = MagicMock(return_value=thriller)
    genre_dao.get_all = MagicMock(return_value=[thriller, drama, horror])
    genre_dao.create = MagicMock(return_value=Genre(id=3))
    genre_dao.update = MagicMock()
    genre_dao.delete = MagicMock()

    return genre_dao


@pytest.fixture
def movie_fixture_dao():
    '''
    We will create a fixture with a mock,
    and here we have 3 instances of the class.
    :return: values for each method in MovieDAO
    '''
    movie_dao = MovieDAO(None)

    avatar = Movie(id=1, title='Avatar')
    the_walkin_dead = Movie(id=2, title='The Walking Dead')
    its = Movie(id=3, title='Its')

    movie_dao.get_one = MagicMock(return_value=avatar)
    movie_dao.get_all = MagicMock(return_value=[avatar, the_walkin_dead, its])
    movie_dao.create = MagicMock(return_value=Movie(id=3))
    movie_dao.update = MagicMock()
    movie_dao.delete = MagicMock()

    return movie_dao