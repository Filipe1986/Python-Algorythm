'''
Preconditions:

Rules :
    The value inside each position in the array is a heigth (y), 
    width(x) distancy between positions in the array
    How can i find the largest volume of water (x * Y)?

Complexity:
    O(N)
'''

def max_area(array):
    size_array = len(array)
    max_area = 0
    if(size_array < 2):
        return -1

    left = 0
    rigth = size_array -1 

    while(left < rigth):
        x =  rigth - left
        shorter_y = min(array[left], array[rigth])
        temp_area = shorter_y * x 

        max_area = max(max_area,  temp_area)

        if( array[left] < array[rigth]):
            left+=1
        else:
            rigth-=1

    return max_area


matrix =[
    #size condition
    [],
    [ 1],
    [ 1, 2], 
    [1, 8, 6, 2, 5, 4, 8, 3, 7],
    [1, 8, 6, 60, 50, 4, 8, 3, 7],
    [1, 8, 6, 60, 50, 20, 4, 8, 3, 7]
   
]

for array in matrix:
    print(max_area(array) )