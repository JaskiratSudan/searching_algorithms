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
            exec_time_micro = (end_time - start_time) * 1e6
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
    n = int(sys.argv[1])
    key = int(sys.argv[2])
    print("The n is:", n, 'Key is:', key, '\n')
    sorted_array, unsorted_array = prepare_integer_array(n, 1, n)
    result = binary_search(sorted_array, key)
    print("Result:", result)
