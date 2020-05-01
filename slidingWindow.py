'''
Python 2.7

Preconditions :

Complexity : 
    O(N)

'''
import math

#Brute force Complexity: O(N^2)
def brute_force(array, window_length):

    max_sum = float("-inf")
    array_length = len(array)
    if(array_length <= 0):
        print("Invalid array")
        return -1

    for i in range(0, array_length -window_length+1):
        current_sun = 0
        for j in range(0, window_length):
            current_sun += array[i+j]
        max_sum = max(current_sun, max_sum)

    return max_sum


def sliding_window(array, window_length):
    array_length = len(array)
    if(array_length <= 0):
        print("Invalid array")
        return -1

    windonw_sum = sum(array[i] for i in range(window_length))
    max_sum = windonw_sum
    

    for i in range(0, array_length -window_length ):
        windonw_sum = windonw_sum - array[i] + array[i+window_length]
        max_sum = max(max_sum, windonw_sum)
    return max_sum

array = []
print("Result bf " + str(brute_force(array, 3)))
print("Result bf " + str(sliding_window(array, 3)))

