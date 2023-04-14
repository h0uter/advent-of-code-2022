import pytest
from day_four import algo


@pytest.fixture
def input_data():
    return [([1, 2, 3, 4], [2, 3]), ([5, 6, 7], [6]), ([8], [10])]


def test_main(input_data):
    assert algo(input_data) == 2
