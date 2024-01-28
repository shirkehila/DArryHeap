from d_ary_heap import DAryHeap
from heap_exceptions import HeapUnderflowError, HeapIndexError, HeapOverflowError
from input_reader import read_input_from_file


def get_validated_choice():
    while True:
        choice = input("Enter your choice (1-5): ")
        if choice.isdigit() and 1 <= int(choice) <= 5:
            return choice
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")


def get_validated_float_input(prompt):
    while True:
        user_input = input(prompt)
        try:
            return float(user_input)
        except ValueError:
            print("Invalid input. Please enter a valid float.")


def get_validated_int_input(prompt):
    while True:
        user_input = input(prompt)
        if user_input.isdigit():
            return int(user_input)
        else:
            print("Invalid input. Please enter a valid integer.")


def cli_extract_max(heap):
    try:
        max_key = heap.extract_max()
        print(f"Maximum key extracted: {max_key}")
    except HeapUnderflowError:
        print("Error: Heap is empty")


def cli_insert(heap):
    new_key = get_validated_float_input("Enter the key to insert: ")
    try:
        heap.insert(new_key)
        print("Key inserted successfully")
    except HeapOverflowError as e:
        print(f"Error: {e}")


def cli_delete(heap):
    index_to_delete = get_validated_int_input("Enter the index to delete: ")
    try:
        heap.delete(index_to_delete)
        print("Node deleted successfully")
    except (ValueError, HeapUnderflowError, HeapIndexError) as e:
        print(f"Error: {e}")


def cli_print_heap(heap):
    print(heap)


def cli_exit_program(heap):
    print("Exiting the program.")
    exit(0)


choice_functions = {
    '1': cli_extract_max,
    '2': cli_insert,
    '3': cli_delete,
    '4': cli_print_heap,
    '5': cli_exit_program
}


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

        choice = get_validated_choice()

        # Call the chosen function using the dictionary
        choice_functions[choice](heap)


if __name__ == "__main__":
    main()
