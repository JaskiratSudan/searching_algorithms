import sys
import time
from array_preparation import prepare_integer_array


def interpolation_search(arr, k):

    start_time = time.perf_counter()
    comparisons = 0
    n = len(arr)

    if n == 0:
        end_time = time.perf_counter()
        exec_time_micro = (end_time - start_time) * 1e6
        return {
            'found': False,
            'index': None,
            'comparisons': comparisons,
            'execution_time_microseconds': exec_time_micro
        }

    low = 0
    high = n - 1
    ascending = arr[low] <= arr[high]

    found_index = None

    # Main interpolation loop
    while low <= high and arr[low] != arr[high]:
        # Check if key is outside the current range
        if ascending:
            if k < arr[low] or k > arr[high]:
                break
        else:
            if k > arr[low] or k < arr[high]:
                break

        # Estimate position
        denominator = (arr[high] - arr[low])
        if denominator == 0:
            break

        pos = low + (high - low) * (k - arr[low]) // denominator

        # Safety check for pos
        if pos < low or pos > high:
            break

        comparisons += 1
        if arr[pos] == k:
            end_time = time.perf_counter()
            exec_time_micro = (end_time - start_time) * 1e6
            return {
                'found': True,
                'index': pos,
                'comparisons': comparisons,
                'execution_time_microseconds': exec_time_micro
            }

        if ascending:
            if arr[pos] < k:
                low = pos + 1
            else:
                high = pos - 1
        else:  # descending
            if arr[pos] < k:
                # smaller values are towards the high end
                high = pos - 1
            else:
                low = pos + 1

    # Final boundary checks if any range is left
    if low <= high:
        comparisons += 1
        if arr[low] == k:
            found_index = low
        elif low != high:
            comparisons += 1
            if arr[high] == k:
                found_index = high

    end_time = time.perf_counter()
    exec_time_micro = (end_time - start_time) * 1e6

    return {
        'found': found_index is not None,
        'index': found_index,
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

    sorted_array, unsorted_array = prepare_integer_array(n, 0, n, reverse)

    print(
        f"\nStarting Interpolation Search Experiment for {array_type} Array "
        f"{'Descending' if reverse else ('Ascending' if array_type == 'sorted' else '')}\n"
    )

    array_to_search = sorted_array
    result = interpolation_search(array_to_search, key)

    print("Result:", result)
