import sys
import time
from array_preparation import prepare_integer_array


def sequential_search(arr, k):
    comparisons = 0
    start_time = time.perf_counter()

    for idx, val in enumerate(arr):
        comparisons += 1
        if val == k:
            end_time = time.perf_counter()
            exec_time_micro = (end_time - start_time) * 1e6
            return {
                'found': True,
                'index': idx,
                'comparisons': comparisons,
                'execution_time_microseconds': exec_time_micro
            }

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
    n = int(sys.argv[1])            # Size of the Array
    key = int(sys.argv[2])          # Key to search
    array_type = sys.argv[3].strip().lower()  # "random" or "sorted"

    try:
        arg = sys.argv[4].strip().lower()
        if arg == "true":
            reverse = True          # Ascending or Descending (for sorted array)
        else:
            reverse = False
    except IndexError:
        reverse = False

    print("The n is:", n, "  Key is:", key, "\n")

    # Random Array Generation (unsorted and sorted version)
    sorted_array, unsorted_array = prepare_integer_array(n, 0, n, reverse)

    print(
        f"\nStarting Sequential Search Experiment for {array_type} Array "
        f"{'Descending' if reverse else ('Ascending' if array_type == 'sorted' else '')}\n"
    )

    # Sequential Search works on both sorted and unsorted arrays
    if array_type == 'random':
        result = sequential_search(unsorted_array, key)
    else:
        result = sequential_search(sorted_array, key)

    print("Result:", result)
