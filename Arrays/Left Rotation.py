from os import *
from sys import *
from collections import *
from math import *

def leftRotationsOfArray(nums, queries):
    # Write your code here.
    result=[]
    for query in queries:
        val=query%len(nums)
        rotate=nums[val:]+nums[:val]
        result.append(rotate)
    return result
    pass