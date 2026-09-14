def factorial(n):
    """
    Calculate the factorial of a non-negative integer n.
    
    Args:
        n (int): The number to calculate the factorial of.
        
    Returns:
        int: The factorial of n.
    """
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers.")
    if n == 0 or n == 1:
        return 1
    
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

if __name__ == "__main__":
    # Test cases
    test_values = [0, 1, 5, 10]
    for val in test_values:
        print(f"Factorial of {val} is {factorial(val)}")
