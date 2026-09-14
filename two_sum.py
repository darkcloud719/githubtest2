def two_sum(nums, target):
    """
    Finds two indices in the list 'nums' such that the values at these indices sum up to 'target'.
    
    Args:
        nums (list[int]): A list of integers.
        target (int): The target sum.
        
    Returns:
        list[int]: A list containing the indices of the two numbers that add up to target.
        Returns an empty list if no such pair exists.
    """
    # Dictionary to store the value and its corresponding index
    # key: number, value: index
    prev_map = {}

    for i, n in enumerate(nums):
        diff = target - n
        if diff in prev_map:
            return [prev_map[diff], i]
        prev_map[n] = i
    
    return []

# Test cases
if __name__ == "__main__":
    test_cases = [
        {"nums": [2, 7, 11, 15], "target": 9, "expected": [0, 1]},
        {"nums": [3, 2, 4], "target": 6, "expected": [1, 2]},
        {"nums": [3, 3], "target": 6, "expected": [0, 1]},
        {"nums": [1, 2, 3], "target": 7, "expected": []},
    ]

    for i, tc in enumerate(test_cases):
        result = two_sum(tc["nums"], tc["target"])
        print(f"Test Case {i+1}: nums={tc['nums']}, target={tc['target']}")
        print(f"Result: {result}, Expected: {tc['expected']} - {'PASSED' if result == tc['expected'] else 'FAILED'}")
        print("-" * 30)
