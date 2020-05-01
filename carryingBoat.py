'''
Preconditions:

Rules :
    A person can't be heavier than a boat capacity
    Each boat carries at most 2 people

Complexity:
    O(N Lon(N)) -> because you need to sort
'''

def carrying_boat(people, boat_capacity):
    people.sort()
    num_boats = 0
    left = 0
    rigth = len(people)-1

    while(left<= rigth):
        if(left == rigth):
            num_boats+=1
            break
        if(people[left]+ people[rigth] <= boat_capacity):
            left +=1

        rigth-=1
        num_boats+=1

    return num_boats



people = [1, 2, 3, 3, 3, 1, 2, 3, 3]
boat_capacity = 3

print(carrying_boat(people, boat_capacity))



