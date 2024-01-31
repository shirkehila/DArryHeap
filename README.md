# DAryHeap Python Implementation

## Introduction

The DAryHeap Python Implementation is an efficient d-ary heap data structure implementation. This codebase provides a comprehensive implementation of the d-ary heap, along with a command-line interface (CLI) for easy interaction and testing.

## Features

- Efficient d-ary heap data structure.
- Command-line interface (CLI) for interactive testing.
- Key operations such as extracting the maximum key, inserting a new key, deleting a node by index, and printing the heap.
- Exception handling for various heap-related scenarios.

## Getting Started

### Prerequisites

- Python 3.x installed on your machine.

### Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/your-username/DAryHeap-Python.git

### Running the CLI

The `input.json` file serves as the configuration file for initializing the d-ary heap with specific parameters. Users can follow these steps to customize the initial state of the heap:

1. Open the `input.json` file in the project directory.

2. Modify the values of `d` and `keys` according to your requirements. The file structure is as follows:

    ```json
    {
      "d": 4,  // The number of children each node can have.
      "keys": [3, 1, 4.2, 1, 5, 19, 2, 6.1, 5, 3]  // Initial list of keys to build the heap.
    }
    ```

    - Adjust the value of `d` to determine the number of children each node can have.
    **Warning:** Setting `d` to 1 may result in poor time complexity and defeat the purpose of using a d-ary heap. A higher `d` typically provides better performance. It's recommended to choose a value greater than 1 for `d` for optimal results.
    - Update the `keys` list with your desired initial keys for building the heap.
    **Warning:** Only up to `5000` keys are supported.


3. Save the changes to the `input.json` file.

4. Run the heap_cli.py program:

    ```bash
    python heap_cli.py
    ```

5. Follow the on-screen instructions to interact with the d-ary heap.