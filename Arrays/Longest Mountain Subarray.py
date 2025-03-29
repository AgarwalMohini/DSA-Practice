from os import *
from sys import *
from collections import *
from math import *

def longestMountain(arr, n):

    # Write your code here.
    if n < 3:
        return 0  
    max_length = 0
    
    for i in range(1, n - 1):  
        if arr[i - 1] < arr[i] > arr[i + 1]:  
            left = i - 1
            while left > 0 and arr[left - 1] < arr[left]:
                left -= 1  
            right = i + 1
            while right < n - 1 and arr[right] > arr[right + 1]:
                right += 1 
            max_length = max(max_length, right - left + 1)
    return max_length