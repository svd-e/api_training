import pytest

from methods import MainMethods


@pytest.fixture(scope="session")
def client():
    client = MainMethods()
    yield client
