def fizz_buzz(n):
    """
    Prints numbers from 1 to n. 
    For multiples of 3, prints "Fizz" instead of the number.
    For multiples of 5, prints "Buzz" instead of the number.
    For multiples of both 3 and 5, prints "FizzBuzz".
    """
    for i in range(1, n + 1):
        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz")
        elif i % 3 == 0:
            print("Fizz")
        elif i % 5 == 0:
            print("Buzz")
        else:
            print(i)

if __name__ == "__main__":
    # Example: Run FizzBuzz up to 100
    fizz_buzz(100)
