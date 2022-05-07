"""Test module
"""


class Calculator:
    """Calculate
    """
    def __init__(self):
        self.name = "Calculator"

    def add(self, x_1, y_1):
        """Add
        """
        print("%s: Add" % self.name)
        return x_1 + y_1

    def multiply(self, x_1, y_1):
        """Multiply
        """
        print("%s: Multiply" % self.name)
        return x_1 * y_1
