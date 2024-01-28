import argparse
import json

from d_ary_heap import DAryHeap
from heap_exceptions import HeapUnderflowError, HeapIndexError, HeapOverflowError


# Import your DAryHeap class and exceptions here

def read_input_from_file(file_path):
    try:
        with open(file_path, 'r') as file:
            data = json.load(file)
            return data.get('d'), data.get('keys', [])
    except FileNotFoundError:
        print(f"Error: File not found - {file_path}")
        exit(1)
    except json.JSONDecodeError:
        print(f"Error: Invalid JSON format in file - {file_path}")
        exit(1)


def main():
    input_file_name = "input.json"
    d, keys = read_input_from_file(input_file_name)

    # Create a DAryHeap instance
    heap = DAryHeap(d, keys)

    while True:
        print("\nChoose an operation:")
        print("1. Extract Max")
        print("2. Insert")
        print("3. Delete (by index)")
        print("4. Print Heap")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            try:
                max_key = heap.extract_max()
                print(f"Maximum key extracted: {max_key}")
            except HeapUnderflowError:
                print("Error: Heap is empty")

        elif choice == '2':
            new_key = float(input("Enter the key to insert: "))
            try:
                heap.insert(new_key)
                print("Key inserted successfully")
            except HeapOverflowError as e:
                print(f"Error: {e}")

        elif choice == '3':
            index_to_delete = int(input("Enter the index to delete: "))
            try:
                heap.delete(index_to_delete)
                print("Node deleted successfully")
            except (ValueError, HeapUnderflowError, HeapIndexError) as e:
                print(f"Error: {e}")

        elif choice == '4':
            print(heap)

        elif choice == '5':
            print("Exiting the program.")
            break

        else:
            print("Invalid choice. Please enter a number between 1 and 5.")


if __name__ == "__main__":
    main()
