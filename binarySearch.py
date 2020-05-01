'''
Python 2.7

Preconditions: 
    Sorted Colletions

Complexity : 
    O( log(n) )

'''

import random

def binarySearch(array, target):
    left = 0
    rigth = len(array)
    
    while(left<= rigth):
        middle = int( left + (rigth - left)/2 )

        if(array[middle] == target):
            return middle
        if(array[middle] < target):
            left = middle +1
        else:
            rigth = middle -1
    return -1




array = [1, 3, 4, 5, 6, 7, 8, 9]

target = random.randint(0,10)
print(target)
result = binarySearch(array, target)
print("Positon " + str(result))