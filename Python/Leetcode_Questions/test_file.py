from typing import List
def itemSearch(arr: List[str], targert: str) -> str:
    arr.sort()

    arr_len = len(arr)
    lower = 0
    upper = arr_len -1
    