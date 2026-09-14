def gcd(a, b):
    """Compute the greatest common divisor of a and b using the Euclidean Algorithm."""
    while b:
        a, b = b, a % b
    return a

def lcm(a, b):
    """Compute the least common multiple of a and b."""
    if a == 0 or b == 0:
        return 0
    return abs(a * b) // gcd(a, b)

if __name__ == "__main__":
    # Test cases
    num1 = 12
    num2 = 18
    print(f"Numbers: {num1}, {num2}")
    print(f"GCD: {gcd(num1, num2)}")  # Expected: 6
    print(f"LCM: {lcm(num1, num2)}")  # Expected: 36

    num3 = 48
    num4 = 18
    print(f"\nNumbers: {num3}, {num4}")
    print(f"GCD: {gcd(num3, num4)}")  # Expected: 6
    print(f"LCM: {lcm(num3, num4)}")  # Expected: 144
