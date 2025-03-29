from typing import List

def kthSmallest(n: int, k: int, arr: List[int]) -> int:
    # write your code here
    arr.sort()
    return arr[k-1]
    pass
