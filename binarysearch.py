import sys
from array_preparation import prepare_integer_array
import time


def binary_search(arr, k):
    left = 0
    right = len(arr) - 1
    comparisons = 0
    start_time = time.perf_counter()

    while left <= right:
        mid = (left + right) // 2
        comparisons += 1
        if arr[mid] == k:
            end_time = time.perf_counter()
            exec_time_micro = (end_time - start_time) * \
                1e6  # Time in Microseconds
            return {
                'found': True,
                'index': mid,
                'comparisons': comparisons,
                'execution_time_microseconds': exec_time_micro
            }
        elif k < arr[mid]:
            right = mid - 1
        else:
            left = mid + 1

    end_time = time.perf_counter()
    exec_time_micro = (end_time - start_time) * 1e6
    return {
        'found': False,
        'index': None,
        'comparisons': comparisons,
        'execution_time_microseconds': exec_time_micro
    }


if __name__ == '__main__':
    # Reading the command line User Input
    n = int(sys.argv[1])  # Size of the Array
    key = int(sys.argv[2])  # Key to search
    array_type = sys.argv[3].strip().lower()  # Random or Sorted array
    try:
        arg = sys.argv[4].strip().lower()
        if arg == "true":
            reverse = True  # Ascending or Descending
        else:
            reverse = False
    except IndexError:
        reverse = False
    print("The n is:", n, '  Key is:', key, '\n')

    # Random Array Generation
    sorted_array, unsorted_array = prepare_integer_array(n, 0, n, reverse)

    print(
        f"\nStarting Binary Search Experiment for {array_type} Array {'Descending' if reverse else ('Ascending' if array_type == 'sorted' else '')}\n")
    # Binary Search
    if array_type == 'random':
        result = binary_search(unsorted_array, key)
    else:
        result = binary_search(sorted_array, key)
    print("Result:", result)
