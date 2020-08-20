'''
Preconditions:

Rules :
    Longest substring without repetetion letters
    Return just the size
Complexity:
    O(N)
'''

def longest_substring(st):
    #hash
    m={}
    left = 0 
    rigth = 0
    answer = 0
    length = len(st)

    while(left < length and rigth < length):
        element = s[rigth]
        if(element in m):
            left = max(left, m[element] +1)
        m[element] = rigth
        answer = max(answer, rigth-left+1)
        rigth+=1
    return answer




print(longest_substring("udhasdioasdhasdgasiud"))

