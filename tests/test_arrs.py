import pytest

from utils import arrs
from utils.arrs import my_slice


def test_get():
    assert arrs.get([1, 2, 3], 1, "test") == 2
    assert arrs.get([], -1, "test") == "test"


@pytest.mark.parametrize('array, starting_index, end_index, expected', [
    ([1, 2, 3, 4], 1, 3, [2, 3]),
    ([1, 2, 3], 1, None, [2, 3]),
    ([], 1, None, []),
    ([1, 2, 3], -4, None, [1, 2, 3]),
    ([1, 2, 3], -2, None, [2, 3])
])
def test_slice(array, starting_index, end_index, expected):
    assert my_slice(array, starting_index, end_index) == expected



