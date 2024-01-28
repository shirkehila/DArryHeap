import json


def read_input_from_file(file_path):
    try:
        with open(file_path, 'r') as file:
            data = json.load(file)
            d = data.get('d')
            keys = data.get('keys', [])

            if not isinstance(keys, list):
                raise ValueError("Error: 'keys' must be a list in the JSON file.")

            if d < 1:
                raise ValueError("Error: 'd' must be positive.")

            if len(keys) > 5000:
                raise ValueError("Error: There are more than 5000 values in 'keys'.")

            # Check that all values in 'keys' are floats
            if not all(isinstance(val, (int, float)) for val in keys):
                raise ValueError("Error: All values in 'keys' must be floats.")

            return d, keys
    except FileNotFoundError:
        print(f"Error: File not found - {file_path}")
        exit(1)
    except json.JSONDecodeError:
        print(f"Error: Invalid JSON format in file - {file_path}")
        exit(1)
    except ValueError as e:
        print(e)
        exit(1)
