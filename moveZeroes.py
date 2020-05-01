'''
Preconditions :

Rules:
    Push the zeros to the end of the array

Complexity : 
    O(N)
'''


def moveZeroes(array):
    j = 0
    for num in array:
        if(num != 0):
            array[j] = num
            j +=1
    for x in range(j, len(array)):
        array[x] = 0
    return array


array = [0 , 1, 0, 30, 12, 0, 0 , 1, 2, 3, 4, 5, 0 , 0, 0]

print(moveZeroes(array))


