from os import *
from sys import *
from collections import *
from math import *

def binaryPuzzle(n):
    #Write your code here.
    rem=""
    while(n>0):
        if(n%2==1):
            rem+='1'
        else:
            rem+='0'
        n=n//2
    return rem[::-1]
    
