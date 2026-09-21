import numpy as np
import pytest

from deque import deque


def test_add_to_tail():
    d = deque(5)

    d.addToTail(np.int32(10))
    d.addToTail(np.int32(20))
    d.addToTail(np.int32(30))

    assert d.accessByIndex(np.int32(0)) == 10
    assert d.accessByIndex(np.int32(1)) == 20
    assert d.accessByIndex(np.int32(2)) == 30


def test_add_to_head():
    d = deque(5)

    d.addToHead(np.int32(10))
    d.addToHead(np.int32(20))
    d.addToHead(np.int32(30))

    assert d.accessByIndex(np.int32(0)) == 30
    assert d.accessByIndex(np.int32(1)) == 20
    assert d.accessByIndex(np.int32(2)) == 10


def test_remove_from_head():
    d = deque(5)

    d.addToTail(np.int32(10))
    d.addToTail(np.int32(20))
    d.addToTail(np.int32(30))

    assert d.removeFromHead() == 10
    assert d.accessByIndex(np.int32(0)) == 20


def test_remove_from_tail():
    d = deque(5)

    d.addToTail(np.int32(10))
    d.addToTail(np.int32(20))
    d.addToTail(np.int32(30))

    assert d.removeFromTail() == 30
    assert d.accessByIndex(np.int32(1)) == 20


def test_overflow():
    d = deque(2)

    d.addToTail(np.int32(10))
    d.addToTail(np.int32(20))

    with pytest.raises(OverflowError):
        d.addToTail(np.int32(30))


def test_remove_from_empty():
    d = deque(5)

    with pytest.raises(IndexError):
        d.removeFromHead()