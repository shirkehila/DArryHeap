class HeapUnderflowError(Exception):
    """Custom exception for heap underflow."""
    def __init__(self, message="Heap underflow"):
        self.message = message
        super().__init__(self.message)