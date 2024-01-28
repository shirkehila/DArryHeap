from random import uniform
import pytest
from d_ary_heap import DAryHeap


@pytest.fixture
def not_heap_100():
    return DAryHeap(5, [n for n in range(1, 100 + 1)], should_build_heap=False)


@pytest.fixture
def not_heap():
    return DAryHeap(2, [1, 2, 3], should_build_heap=False)


@pytest.fixture
def random_max_heap():
    random_float_array = [uniform(0, 100) for _ in range(20)]
    max_heap = DAryHeap(3, random_float_array)
    return max_heap


def check_max_heap_property(heap, index):
    key = heap.get_key(index)
    for child_number in range(1, heap.d + 1):
        child_index = heap.child(index, child_number)
        if child_index <= heap.heap_size:
            child_key = heap.get_key(child_index)
            assert key >= child_key
            check_max_heap_property(heap, child_index)


def test_max_heap_property(random_max_heap):
    check_max_heap_property(random_max_heap, 1)


def test_child_index(not_heap_100):
    assert not_heap_100.get_key(not_heap_100.child(2, 3)) == 9


def test_child_and_parent_indices(not_heap_100):
    parent_index = 2
    for child_number in range(1, not_heap_100.d + 1):
        child_index = not_heap_100.child(parent_index, child_number)
        assert not_heap_100.parent(child_index) == parent_index


def test_max_heapify(not_heap):
    parent_index = 1
    not_heap.max_heapify(parent_index)
    assert not_heap.get_key(parent_index) == 3


def test_insert(random_max_heap):
    random_max_heap.insert(50)
    check_max_heap_property(random_max_heap, 1)


def test_array_size(random_max_heap):
    assert len(random_max_heap.heap) == random_max_heap.capacity + 1