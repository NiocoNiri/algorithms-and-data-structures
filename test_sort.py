import pytest

from buble_sort import buble_sort
from fast_sort import fast_sort


@pytest.mark.parametrize("sort", [buble_sort, fast_sort])
@pytest.mark.parametrize("values", [
    [],
    [1],
    [3, 1, 2],
    [1, 2, 3],
    [3, 2, 1],
    [2, 1, 2],
    [-3, 0, -1],
    [4, 4, 4, 4],
])
def test_sort(sort, values):
    assert sort(values.copy()) == sorted(values)
