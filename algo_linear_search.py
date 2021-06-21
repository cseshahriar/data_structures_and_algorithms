"""
Linear Search Algorithom:
input: one list L and an element X
output: list index i, where element found if not found i = -1
step 1: list item of n
step 2: i value 0 to (n-1) increse by 1 and every value for go step 3
step 3: L[i] and x is equal to, if is so return i
step 4: i are value -1 take

easy:
step 1: L elements n
step 2: i = 0 take
step 3: i is less than n? then go step 4 else go step 7
step 5: i return(founded)
step 6: i value increse are go step 3
step 7: i = -1  are i return
"""

def linear_search(L, x):
    n = len(L) # step 1 
    i = 0 # step 2

    while i < n: # step 3
        if L[i] == x: # step 4
            return i  # step 5

        i += 1 # step 6
    i = -1 # step 7

    return i


def linear_search_py(L, x):
    """python efficent code"""
    n = len(L) # list length

    for i in range(n):
        if L[i] == x: # compare if the search value in list
            return i

    return -1


result = linear_search_py([1,4,5,7], 8)
print(result) # position