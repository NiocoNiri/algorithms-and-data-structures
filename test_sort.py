import pytest
from random import randint
from buble_sort import buble_sort
from fast_sort import fast_sort

@pytest.mark.parametrize("a", [
    [],
    [1],
    [3, 1, 2],
    [1, 2, 3],
    [3, 2, 1],
    [2, 1, 2],
    [-3, 0, -1],
])
def test_buble_sort(a):
    expected = sorted(a)
    assert buble_sort(a) == expected

def test_fast_sort(a):
    expected = sorted(a)
    assert fast_sort(a) == expected
