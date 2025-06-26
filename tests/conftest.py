import pytest

from data import mock



@pytest.fixture
def bun():
    return mock.bun_mock()


@pytest.fixture
def ingridient():
    return mock.ingridient_mock()


@pytest.fixture
def ingridient_2():
    return mock.ingridient_2_mock()
