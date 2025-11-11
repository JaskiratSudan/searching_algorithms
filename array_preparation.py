from random import randint
from typing import List, Tuple


def prepare_integer_array(
    size: int,
    min_value: int = 0,
    max_value: int = 100,
) -> Tuple[List[int], List[int]]:
    if size < 0:
        raise ValueError("size must be non-negative")
    if min_value > max_value:
        raise ValueError("min_value must be less than or equal to max_value")

    unsorted: List[int] = [randint(min_value, max_value) for _ in range(size)]
    sorted_version: List[int] = sorted(unsorted)
    return unsorted, sorted_version
