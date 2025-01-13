#!/usr/bin/python3
import sys


def factorial(n):
    """
    Computes the factorial of a non-negative integer n using recursion.

    The factorial of number n is the product of integers less than or equal n
    For example:
    - factorial(0) = 1
    - factorial(5) = 5 * 4 * 3 * 2 * 1 = 120

    Args:
    - n (int): The number for which the factorial needs to be calculated.

    Returns:
    - int: The factorial of the input number n.

    Raises:
    - RecursionError: If the recursion depth exceeds the maximum limit.
    """
    if n == 0:
        return 1  # Base case: the factorial of 0 is defined as 1
    else:
        return n * factorial(n - 1)  # Recursive case: n * factorial of n-1

# Check if the script is being executed with a command-line argument.
# sys.argv is a list where sys.argv[0] is the script name
# This assumes the user has provided an argument for the factorial calculation.


try:
    # Convert the first command-line argument to an integer and calculate
    f = factorial(int(sys.argv[1]))
    print(f)  # Print the computed factorial.
except IndexError:
    print(
        "Error: No argument provided. Please provide a number to "
        "calculate the factorial."
    )
except ValueError:
    print("Error: Invalid input. Please provide a valid integer.")
