from unittest.mock import MagicMock

import pytest

from dao.genre import GenreDAO
from dao.model.genre import Genre


@pytest.fixture
def genre_dao():
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
