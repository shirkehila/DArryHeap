from random import uniform
from typing import List
from math import floor, log

from heap_exceptions import HeapUnderflowError, HeapOverflowError, HeapIndexError


class DAryHeap:
    def __init__(self, d: int, keys: List[float], capacity: int = 5000, should_build_heap: bool = True):
        """
        Initializes a d-ary heap.

        :param d: The number of children each node can have.
        :param keys: Initial list of keys to build the heap.
        :param capacity: Maximum capacity of the heap.
        :param should_build_heap: Flag to determine whether to build the heap during initialization.
        """
        self.d: int = d
        self.capacity: int = capacity
        # Using None for empty slots in the heap, with the actual keys starting from index 1
        self.heap: List[float] = [None] + keys + [None for _ in range(capacity - len(keys))]
        self.heap_size: int = len(keys)
        if should_build_heap:
            self.build_max_heap()

    def build_max_heap(self) -> None:
        """
        Builds a max heap from the given list of keys.
        """
        d: int = self.d
        n: int = self.heap_size
        last_non_leaf_index: int = floor((n + d - 2) / d)
        for i in range(last_non_leaf_index, 0, -1):
            self.max_heapify(i)

    def child(self, i: int, child_number: int) -> int:
        """
        Calculates the index of the child at the given child_number for the node at index i.

        :param i: Index of the parent node.
        :param child_number: The ordinal number of the child, starting from 1.
        :return: Index of the child.
        """
        d: int = self.d
        second_to_last_child: int = d * i
        return second_to_last_child - (d - 1) + child_number

    def parent(self, i: int) -> int:
        """
        Calculates the index of the parent node for the node at index i.

        :param i: Index of the child node.
        :return: Index of the parent.
        """
        d: int = self.d
        return floor((i + d - 2) / d)

    def get_key(self, i: int) -> float:
        """
        Gets the key of the node at index i.

        :param i: Index of the node.
        :return: Key of the node.
        :raises: HeapIndexError if the index is out the heap bounds
        """
        if i > self.heap_size:
            raise HeapIndexError
        return self.heap[i]

    def set_key(self, i: int, key: float) -> None:
        """
        Sets the key of the node at index i.

        :param i: Index of the node.
        :param key: New key value.
        """
        self.heap[i] = key

    def exchange(self, i1: int, i2: int) -> None:
        """
        Exchanges the positions of two nodes in the heap.

        :param i1: Index of the first node.
        :param i2: Index of the second node.
        """
        self.heap[i1], self.heap[i2] = self.heap[i2], self.heap[i1]

    def max_heapify(self, i: int) -> None:
        """
        Maintains the max heap property by adjusting the node at index i.
        Assumes the rest of the heap rooted at that index satisfies the max-heap property.

        :param i: Index of the node to be heapified.
        """
        largest: int = i
        largest_key: float = self.get_key(i)
        children_indices: List[int] = self.get_children(i)
        for child_index in children_indices:
            child_key: float = self.get_key(child_index)
            if child_key > largest_key:
                largest = child_index
                largest_key = child_key
        if largest != i:
            self.exchange(largest, i)
            self.max_heapify(largest)

    def extract_max(self) -> float:
        """
        Extracts the maximum key from the heap.

        :return: The maximum key.
        :raises HeapUnderflowError: If the heap is empty.
        """
        if self.heap_size == 0:
            raise HeapUnderflowError()
        max_key: float = self.heap[1]
        self.heap[1] = self.heap[self.heap_size]
        self.heap_size -= 1
        self.max_heapify(1)
        return max_key

    def get_children(self, i: int) -> List[int]:
        """
        Gets the indices of the children of the node at index i.

        :param i: Index of the parent node.
        :return: List of indices of the children.
        """
        # First assume d children
        possible_children_indices: List[int] = [self.child(i, child_number) for child_number in range(1, self.d + 1)]
        # Now check which of them are actually part of the heap
        return [child_index for child_index in possible_children_indices if child_index <= self.heap_size]

    def str_heap(self, i: int) -> str:
        """
        Generates a string representation of the subtree rooted at the node with index i.

        :param i: Index of the root of the subtree.
        :return: String representation of the subtree.
        """
        result: str = f"{self.get_key(i)}\n"
        children_indices: List[int] = self.get_children(i)
        for child_number, child_index in enumerate(children_indices, start=1):
            nodes: List[str] = self.str_heap(child_index).split("\n")
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

    def __str__(self) -> str:
        """
        Generates a string representation of the entire heap.

        :return: String representation of the heap.
        """
        if self.heap_size == 0:
            return "Heap is empty"
        return "Heap:\n" + self.str_heap(1)

    def heap_increase_key(self, i: int, key: float) -> None:
        """
        Increases the key of the node at index i to the new key value.
        Doing that while maintaining the max heap property.

        :param i: Index of the node.
        :param key: New key value.
        :raises ValueError: If the new key is smaller than the current key.
        """
        current_key: float = self.get_key(i)
        if key < current_key:
            raise ValueError(f"New key {key} is smaller than current key {current_key}")
        self.set_key(i, key)
        while i > 1 and self.get_key(self.parent(i)) < self.get_key(i):
            self.exchange(i, self.parent(i))
            i = self.parent(i)

    def insert(self, key: float) -> None:
        """
        Inserts a new key into the heap.

        :param key: Key to be inserted.
        :raises HeapOverflowError: If the heap is already at maximum capacity.
        """
        if self.capacity < self.heap_size + 1:
            raise HeapOverflowError
        self.heap_size += 1
        self.set_key(self.heap_size, float('-inf'))
        self.heap_increase_key(self.heap_size, key)

    def delete(self, index: int) -> None:
        """
        Deletes the node at the given index from the heap.

        :param index: Index of the node to be deleted.
        """
        self.heap_increase_key(index, float('inf'))
        self.extract_max()
