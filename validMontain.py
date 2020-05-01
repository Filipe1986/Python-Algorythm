'''
Rules :
    Array size >= 3
    no repeatition
    increase numbers then decrease numbers ^

Preconditions:

Complexity:
    O(N)
'''

def validMontain(array):
    increasing = True
    size = len(array)

    if(size <= 2 or array[1] >= array[2]):
        return False
    count = 0

    for i in range(0, size-1):
        if(array[i] > array[i+1] and increasing):
            increasing = False
        elif((array[i] <=  array[i+1] and (not increasing)) 
                or array[i] ==  array[i+1]):
            return False
    return True


array =[
    #size condition
    [],
    [ 1],
    [ 1, 2], 
    # 
    [ 3, 2, 1],# not increasing beginning
    #
    [ 1, 0, 1, 3, 5, 3], #Decrease beginning condition
    [ 1, 2, 3, 1, 2, 1], #Middle condition
    [ 0, 1, 3, 5, 3, 7], #Decrease end condition
    [ 1, 2, 3, 3, 2, 1], #repeated condition
    [ 0, 1,  2, 3, 5, 3, 2], #True
    
]

for i in array:
    print(validMontain(i) )