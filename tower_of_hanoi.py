def tower_of_hanoi(n, source, destination, auxiliary):
    """
    Solves the Tower of Hanoi puzzle recursively.

    Args:
        n (int): Number of disks to move.
        source (str): The name of the starting rod.
        destination (str): The name of the target rod.
        auxiliary (str): The name of the intermediate rod.

    Returns:
        None: Prints the sequence of moves to the console.

    Logic:
        1. Move n-1 disks from source to auxiliary.
        2. Move the largest disk (n) from source to destination.
        3. Move n-1 disks from auxiliary to destination.
    """
    # Base case: only one disk to move
    if n == 1:
        print(f"Move disk 1 from {source} to {destination}")
        return
    # Move n-1 disks from source to auxiliary
    tower_of_hanoi(n - 1, source, auxiliary, destination)
    # Move the nth disk from source to destination
    print(f"Move disk {n} from {source} to {destination}")
    # Move n-1 disks from auxiliary to destination
    tower_of_hanoi(n - 1, auxiliary, destination, source)

if __name__ == "__main__":
    n_disks = 3
    tower_of_hanoi(n_disks, 'A', 'C', 'B')
