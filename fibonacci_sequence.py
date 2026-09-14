def fibonacci(n):
    """
    Generate a Fibonacci sequence up to n terms.

    Args:
        n (int): The number of terms to generate.

    Returns:
        list: A list containing the Fibonacci sequence.
    """
    # Initialize the sequence with the first two Fibonacci numbers
    sequence = [0, 1]
    # Iteratively calculate the next term by summing the previous two
    while len(sequence) < n:
        sequence.append(sequence[-1] + sequence[-2])
    # Return the sequence, sliced to handle cases where n < 2
    return sequence[:n]


if __name__ == "__main__":
    num_terms = 10
    print(f"Fibonacci sequence ({num_terms} terms): {fibonacci(num_terms)}")

import unittest

class TestFibonacci(unittest.TestCase):
    def test_fibonacci_sequence(self):
        self.assertEqual(fibonacci(0), [])
        self.assertEqual(fibonacci(1), [0])
        self.assertEqual(fibonacci(2), [0, 1])
        self.assertEqual(fibonacci(5), [0, 1, 1, 2, 3])
        self.assertEqual(fibonacci(10), [0, 1, 1, 2, 3, 5, 8, 13, 21, 34])

if __name__ == "__main__":
    unittest.main()
