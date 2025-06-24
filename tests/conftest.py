from unittest.mock import Mock

import pytest

from burger import Burger


@pytest.fixture
def burger():
    return Burger()


@pytest.fixture
def bun():
    bun = Mock()
    bun.get_name.return_value = "булочка"
    bun.get_price.return_value = 404.0
    return bun


@pytest.fixture
def ingridient():
    ingridient = Mock()
    ingridient.get_price.return_value = 404.4
    ingridient.get_name.return_value = "колбаса"
    ingridient.get_type.return_value = "мясо"
    return ingridient


@pytest.fixture
def ingridient_2():
    ingridient = Mock()
    ingridient.get_price.return_value = 111.1
    ingridient.get_name.return_value = "ананас"
    ingridient.get_type.return_value = "фрукт"
    return ingridient
