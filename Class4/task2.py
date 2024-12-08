import numpy as np
#### 1. Create a random vector of size N and find the mean value
def rand_mean(N: int) -> float:
 
    if not isinstance(N, int):
        raise TypeError("N должно быть целым числом.")
    if N <= 0:
        raise ValueError("N должно быть положительным целым числом.")

    return np.mean(np.random.rand(N))


# Пример использования с обработкой ошибок
try:
    print("Задача 1: ", rand_mean(10))
    print("Задача 2: ", rand_mean(0)) 
except (TypeError, ValueError) as e:
    print(f"Ошибка: {e}")

    import numpy as np
from memory_profiler import memory_usage


## потенциальное решение
import numpy as np

def rand_mean(N):
    """
    Generate a random vector of size N and return its mean value.

    Args:
        N (int): Size of the random vector. Must be a positive integer.

    Returns:
        float: Mean value of the random vector.

    Raises:
        ValueError: If N is not a positive integer.
    """
    if not isinstance(N, int) or N <= 0:
        raise ValueError("N must be a positive integer.")
    
    random_vector = np.random.rand(N)  # Generate random vector
    return random_vector.mean()       # Calculate and return mean

# Example usage with error handling
try:
    print("Task 1: Mean =", rand_mean(10))  # Should work
    print("Task 2: Mean =", rand_mean(0))   # Will raise an error
except ValueError as e:
    print("Error:", e)

#### 2. Create a 8x8 matrix and fill it with a checkerboard pattern
def print_checkerboard():
    
   
    checkboard = np.tile([0,1], (8,4)) % 2  
    print("Задача 2: \n", checkboard)


def memory_usage_checkerboard():
   
    mem_usage = memory_usage((print_checkerboard, ), interval=0.1, max_usage=True)
    print(f"Использовано памяти для шахматной доски: {mem_usage:.2f} MiB")


# Пример использования:
print_checkerboard()
memory_usage_checkerboard()

import numpy as np
from memory_profiler import memory_usage  # Ensure you have memory_profiler installed

def create_checkerboard():
    """
    Create an 8x8 matrix with a checkerboard pattern.
    
    Returns:
        np.ndarray: 8x8 checkerboard pattern matrix.
    """
    # Generate an 8x8 checkerboard pattern
    checkerboard = np.zeros((8, 8), dtype=int)
    checkerboard[1::2, ::2] = 1  # Fill 1s on odd rows, even columns
    checkerboard[::2, 1::2] = 1  # Fill 1s on even rows, odd columns
    return checkerboard

def print_checkerboard():
    """
    Print the 8x8 checkerboard matrix.
    """
    checkerboard = create_checkerboard()
    print("Task 2: Checkerboard Pattern:")
    print(checkerboard)

def memory_usage_checkerboard():
    """
    Calculate and display memory usage of creating the checkerboard pattern.
    """
    mem_usage = memory_usage((create_checkerboard,), interval=0.1, max_usage=True)
    print(f"Memory used for checkerboard: {mem_usage:.2f} MiB")

# Example usage
print_checkerboard()
memory_usage_checkerboard()


#### 3. Print the minimum and maximum representable value for each numpy scalar type
import numpy as np

def min_max_repr():
    
    dtypes = [np.int8, np.int32, np.int64, np.float32, np.float64]
    for dtype in dtypes:
        if np.issubdtype(dtype, np.integer):
            info = np.iinfo(dtype)
            print(f"Data type: {dtype}, Min: {info.min}, Max: {info.max}")
        elif np.issubdtype(dtype, np.floating):
            info = np.finfo(dtype)
            print(f"Data type: {dtype}, Min: {info.min}, Max: {info.max}")
        else:
            print(f"Data type: {dtype} is not an integer or floating-point type.")


min_max_repr()

#### 4. How to get the n largest values of an array?
import numpy as np

def n_largest(n: int, arr: np.array = None) -> np.array:
  
    if arr is None:
        arr = np.arange(10000)
        np.random.shuffle(arr)  #Only if you need to test with a random array
    
    if n <= 0 or arr.size == 0:
        return np.array([])

    return arr[np.argpartition(arr, -n)[-n:]]

# Пример использования:
print(n_largest(5))
my_array = np.array([3, 1, 4, 1, 5, 9, 2, 6])
print(n_largest(3, my_array)) 

#### 5. How to compute ((A+B)*(-A/2)) in place (without copy)?

import numpy as np
from memory_profiler import profile


@profile
def compute_in_place_optimized():
    A = np.ones(3)
    B = np.ones(3) * 2

    
    np.add(A, B, out=A)

   
    A *= -0.5

  
    np.multiply(A, B, out=A)
    return A


@profile
def compute_in_place_not_optimized():
    A = np.ones(3)
    B = np.ones(3) * 2
    C = (A + B) * (-A / 2)
    return C


if __name__ == "__main__":
    result_optimized = compute_in_place_optimized()
    print("Оптимизированный результат:", result_optimized)

    result_not_optimized = compute_in_place_not_optimized()
    print("Не оптимизированный результат:", result_not_optimized)
