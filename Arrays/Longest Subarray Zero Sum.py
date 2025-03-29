from math import *
from collections import *
from sys import *
from os import *

def LongestSubsetWithZeroSum(arr):

    # Write your Code here.
    # Return an integer denoting the answer.
    maxLen = 0
    prefix_sum = 0
    index_map = {}  
    for i in range(len(arr)):
        prefix_sum += arr[i]
        if prefix_sum == 0:
            maxLen = i + 1
        if prefix_sum in index_map:
            maxLen = max(maxLen, i - index_map[prefix_sum])
        else:
            index_map[prefix_sum] = i

    return maxLen
    
    pass