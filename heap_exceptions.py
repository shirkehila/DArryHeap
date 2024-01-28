class HeapUnderflowError(Exception):
    """Custom exception for heap underflow."""

    def __init__(self, message="Heap underflow"):
        self.message = message
        super().__init__(self.message)


class HeapOverflowError(Exception):
    """Custom exception for heap overflow."""

    def __init__(self, message="Heap overflow"):
        self.message = message
        super().__init__(self.message)
