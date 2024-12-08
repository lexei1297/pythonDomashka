import numpy as np
from memory_profiler import memory_usage

#### Task 1: Create a random vector of size N and find the mean value
def rand_mean(N: int) -> float:
    """
    Generate a random vector of size N and return its mean value.

    Args:
        N (int): Size of the random vector.

    Returns:
        float: Mean value of the random vector.
    """
    if N <= 0:
        raise ValueError("N must be a positive integer.")
    return np.random.rand(N).mean()

# Example usage:
print("Task 1: Mean of random vector =", rand_mean(10))


#### Task 2: Create an 8x8 matrix and fill it with a checkerboard pattern
def print_checkerboard():
    """
    Create an 8x8 checkerboard pattern matrix and print it.
    """
    checkerboard = np.zeros((8, 8), dtype=np.uint8)
    checkerboard[1::2, ::2] = 1
    checkerboard[::2, 1::2] = 1
    print("Task 2: Checkerboard Pattern:\n", checkerboard)

# Example usage:
print_checkerboard()


#### Task 3: Print the minimum and maximum representable value for each numpy scalar type
def min_max_repr():
    """
    Print the minimum and maximum representable values for various numpy scalar types.
    """
    for dtype in [np.int8, np.int32, np.int64]:
        print(f"Integer type {dtype}: {np.iinfo(dtype)}")
    for dtype in [np.float32, np.float64]:
        print(f"Floating-point type {dtype}: {np.finfo(dtype)}")

# Example usage:
min_max_repr()


#### Task 4: Get the n largest values of an array
def n_largest(n: int) -> np.ndarray:
    """
    Get the n largest values from a shuffled array of integers from 0 to 9999.

    Args:
        n (int): Number of largest elements to find.

    Returns:
        np.ndarray: Array of n largest values.
    """
    if n <= 0:
        raise ValueError("n must be a positive integer.")
    A = np.arange(10000)
    np.random.shuffle(A)
    return np.sort(A)[-n:]  # Sort the last n elements

# Example usage:
print("Task 4: n largest values =", n_largest(5))


#### Task 5: Compute ((A+B)*(-A/2)) in place (without copy)
def compute_in_place():
    """
    Compute ((A+B)*(-A/2)) in place, without creating copies of the arrays.

    Returns:
        np.ndarray: Result of the computation.
    """
    A = np.ones(3) * 1
    B = np.ones(3) * 2
    np.add(A, B, out=B)       # B = A + B
    np.divide(A, 2, out=A)    # A = A / 2
    np.negative(A, out=A)     # A = -A
    np.multiply(A, B, out=A)  # A = A * B
    return A

def compute_in_place_with_copy():
    """
    Compute ((A+B)*(-A/2)) without in-place operations (creates a copy).

    Returns:
        np.ndarray: Result of the computation.
    """
    A = np.ones(3) * 1
    B = np.ones(3) * 2
    return (A + B) * (-A / 2)

# Example usage:
print("Task 5 (in place):", compute_in_place())
print("Task 5 (with copy):", compute_in_place_with_copy())


#### Memory usage comparison for Task 5
def memory_usage_comparison():
    """
    Compare memory usage between in-place and non-in-place operations for Task 5.
    """
    mem_in_place = memory_usage(compute_in_place)
    mem_with_copy = memory_usage(compute_in_place_with_copy)
    print("Memory usage (in place):", mem_in_place)
    print("Memory usage (with copy):", mem_with_copy)

# Example usage:
memory_usage_comparison()
