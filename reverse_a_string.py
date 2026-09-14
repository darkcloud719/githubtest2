def reverse_a_string(s):
    """
    Reverses a given string.
    
    Args:
        s (str): The string to be reversed.
        
    Returns:
        str: The reversed string.
    """
    return s[::-1]

if __name__ == "__main__":
    # Test cases
    test_strings = ["hello", "world", "Python", "12345", ""]
    for ts in test_strings:
        print(f"Original: '{ts}' -> Reversed: '{reverse_a_string(ts)}'")
