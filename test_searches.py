import random
from array_preparation import prepare_integer_array
from sequential_search import sequential_search
from binarysearch import binary_search
from interpolation_search import interpolation_search

ARRAY_SIZES = [100, 1000, 10000]


def run_all():
    algorithms = [
        ("Sequential", sequential_search),
        ("Binary", binary_search),
        ("Interpolation", interpolation_search),
    ]

    for n in ARRAY_SIZES:
        # Generate arrays (ascending sorted + unsorted random)
        sorted_array, unsorted_array = prepare_integer_array(n, 0, n, reverse=False)
        descending_array = sorted_array[::-1]

        key_present_random = random.choice(unsorted_array)
        key_present_sorted = random.choice(sorted_array)
        key_not_present = max(sorted_array) + 1  # guaranteed not in array

        print(f"\n================ n = {n} ================\n")

        for name, func in algorithms:
            print(f"-- {name} Search --")

            # Case 1: Random array, key present
            arr1 = unsorted_array if name == "Sequential" else sorted_array
            res1 = func(arr1, key_present_random)
            print(
                f"Case 1 (Random, present):     "
                f"comps={res1['comparisons']}, "
                f"time_us={res1['execution_time_microseconds']:.2f}"
            )

            # Case 2: Random array, key not present
            arr2 = unsorted_array if name == "Sequential" else sorted_array
            res2 = func(arr2, key_not_present)
            print(
                f"Case 2 (Random, absent):      "
                f"comps={res2['comparisons']}, "
                f"time_us={res2['execution_time_microseconds']:.2f}"
            )

            # Case 3: Sorted ascending, key present
            res3 = func(sorted_array, key_present_sorted)
            print(
                f"Case 3 (Sorted asc, present): "
                f"comps={res3['comparisons']}, "
                f"time_us={res3['execution_time_microseconds']:.2f}"
            )

            # Case 4: Sorted descending, key not present
            if name == "Sequential":
                arr4 = descending_array
            else:
                arr4 = sorted_array

            res4 = func(arr4, key_not_present)
            print(
                f"Case 4 (Sorted desc, absent): "
                f"comps={res4['comparisons']}, "
                f"time_us={res4['execution_time_microseconds']:.2f}"
            )

            print()


if __name__ == "__main__":
    run_all()
