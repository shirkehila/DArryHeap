from typing import List
from math import floor, log

from heap_exceptions import HeapUnderflowError


class DAryHeap:
    def __init__(self, d: int, keys: List[float],capacity: int=5000, should_build_heap: bool = True):
        self.d = d
        self.heap = [None] + keys
        self.heap_size = len(keys)
        if should_build_heap:
            self.build_max_heap()

    def build_max_heap(self):
        d = self.d
        n = self.heap_size
        last_non_leaf_index = floor((n + d - 2) / d)
        for i in range(last_non_leaf_index, 0, -1):
            self.max_heapify(i)

    def child(self, i: int, child_number: int) -> int:
        d = self.d
        second_to_last_child = d * i
        return second_to_last_child - (d - 1) + child_number

    def parent(self, i: int) -> int:
        d = self.d
        return floor((i + d - 2) / d)

    def get_key(self, i: int) -> float:
        return self.heap[i]

    def set_key(self, i: int, key: float):
        self.heap[i] = key

    def exchange(self, i1: int, i2: int):
        self.heap[i1], self.heap[i2] = self.heap[i2], self.heap[i1]

    def max_heapify(self, i: int):
        d = self.d
        largest = i
        largest_key = self.get_key(i)
        for child_number in range(1, d + 1):
            child_index = self.child(i, child_number)
            if child_index <= self.heap_size:
                child_key = self.get_key(child_index)
                if child_key > largest_key:
                    largest = child_index
                    largest_key = child_key
        if largest != i:
            self.exchange(largest, i)
            self.max_heapify(largest)

    def extract_max(self) -> float:
        if self.heap_size == 0:
            raise HeapUnderflowError()
        max_key = self.heap[1]
        self.heap[1] = self.heap[self.heap_size]
        self.heap_size -= 1
        self.max_heapify(1)
        return max_key

    def get_number_of_levels(self):
        d = self.d
        n = self.heap_size
        return floor(log((n - 1) * (d - 1) + 1, d))

    def get_children(self, i):
        possible_children_indices = [self.child(i, child_number) for child_number in range(1, self.d + 1)]
        return [child_index for child_index in possible_children_indices if child_index <= self.heap_size]

    def str_heap(self, i):
        result = f"{self.get_key(i)}\n"
        children_indices = self.get_children(i)
        for child_number, child_index in enumerate(children_indices, start=1):
            nodes = self.str_heap(child_index).split("\n")
            for j, node in enumerate(nodes, start=1):
                if child_number != len(children_indices) and j == 1:
                    result += f"├── {node}\n"
                elif child_number != len(children_indices) and j > 1:
                    result += f"│   {node}\n"
                elif child_number == len(children_indices) and j == 1:
                    result += f"└── {node}\n"
                else:
                    result += f"    {node}\n"
        return result.strip()

    def __str__(self):
        if self.heap_size == 0:
            return "Heap is empty"
        return "Heap:\n" + self.str_heap(1)

    def heap_increase_key(self, i, key):
        current_key = self.get_key(i)
        if key < current_key:
            raise ValueError(f"New key {key} is smaller then current key {current_key}")
        self.set_key(i, key)
        while i > 1 and self.get_key(self.parent(i)) < self.get_key(i):
            self.exchange(i, self.parent(i))
            i = self.parent(i)

    def should_enlarge_array(self, needed_capacity: int) -> bool:
        array_capacity = len(self.heap) - 1
        return needed_capacity > array_capacity

    def insert(self, key):
        if self.should_enlarge_array(needed_capacity=self.heap_size + 1):
            self.heap.append(float('-inf'))
        else:
            self.set_key(self.heap_size + 1, float('-inf'))
        self.heap_size += 1
        self.heap_increase_key(self.heap_size, key)


if __name__ == '__main__':
    h = DAryHeap(3, [3 * n for n in range(1, 10 + 1)])
    print(h)
    m = h.extract_max()
    print(f"m is: {m}")
    print(h)
    h.insert(28)
    print(h)
    h.insert(100)
    print(h)
