"""
This module provides a function to generate and print a multiplication table.
"""

def print_multiplication_table(size=9):
    """
    Generates and prints a multiplication table of a given size.

    The function uses nested loops to calculate the product of two integers
    ranging from 1 up to the specified size. Each product is printed
    with a width of 3 characters for alignment.

    Parameters:
    size (int): The upper limit of the multiplication table. Defaults to 9.

    Returns:
    None: This function prints the output directly to the console.
    """
    for i in range(1, size + 1):
        # Inner loop to calculate products for the current row
        for j in range(1, size + 1):
            # Print the product formatted to 3 spaces, end with a space instead of newline
            print(f"{i * j:3}", end=" ")
        # Print a newline character to move to the next row
        print()

if __name__ == "__main__":
    # Execute the function to print a 9x9 multiplication table
    print_multiplication_table(9)

import unittest
from io import StringIO
import sys

class TestMultiplicationTable(unittest.TestCase):
    def test_print_multiplication_table_output(self):
        captured_output = StringIO()
        sys.stdout = captured_output
        print_multiplication_table(2)
        sys.stdout = sys.__stdout__
        expected_output = "  1   2 \n  2   4 \n"
        self.assertEqual(captured_output.getvalue(), expected_output)

if __name__ == "__main__":
    # Execute the function to print a 9x9 multiplication table
    print_multiplication_table(9)
    # Run tests if executed as a script
    unittest.main(argv=['first-arg-is-ignored'], exit=False)
