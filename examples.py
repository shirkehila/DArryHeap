from d_ary_heap import DAryHeap

# Example 1: Initializing a heap and using extract_max
heap1 = DAryHeap(d=3, keys=[4.5, 10.2, 3.7, 5.1, 1.8, 8.3, 6.6, 9.9, 2.4])
print("Original Heap:")
print(heap1)

max_key = heap1.extract_max()
print(f"Extracted Maximum Key: {max_key}")
print("Heap after extract_max:")
print(heap1)

# Example 2: Initializing a heap and using heap_increase_key
heap2 = DAryHeap(d=2, keys=[8.3, 5.7, 3.2, 12.6, 9.4, 7.8, 10.1, 6.9, 11.2])
print("Original Heap:")
print(heap2)

heap2.heap_increase_key(4, 12.0)
print("Heap after heap_increase_key(4, 12.0):")
print(heap2)

# Example 3: Initializing a heap and using insert
heap3 = DAryHeap(d=4, keys=[7.1, 20.4, 14.8, 8.2, 11.5, 18.7, 15.3, 10.6, 13.9])
print("Original Heap:")
print(heap3)

heap3.insert(15.2)  # Choosing a value that doesn't become the maximum
print("Heap after insert(15.2):")
print(heap3)

# Example 4: Initializing a heap and using delete
heap4 = DAryHeap(d=2, keys=[15.2, 10.6, 5.3, 8.7, 12.9, 14.4, 9.8, 11.3, 7.5])
print("Original Heap:")
print(heap4)

heap4.delete(2)
print("Heap after delete(2):")
print(heap4)

# Example 5: Initializing a heap with d=1
heap5 = DAryHeap(d=1, keys=[5.3, 9.8, 12.1, 7.5, 15.6, 8.9, 10.2, 6.7])
print("Heap with d=1:")
print(heap5)

max_key_5 = heap5.extract_max()
print(f"Extracted Maximum Key: {max_key_5}")
print("Heap after extract_max:")
print(heap5)
