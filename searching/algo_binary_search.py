"""
Binery Search Algorithom:
input: a List L and a element
output: list index i, where  found the element else i = -1

step 1:  take, L value -1
step 2:  left = 0 are right = n -1 not found, left to right index  search
step 3: if left > right is then go step 4
step 4: mid = (left + right) / 2 take, mid is left to right middle index
step 5: L[mid] == x is? return mid 
step 6: L[mid] < x is? left = mid + 1 no found, go step 3
step 7: L[mid] > x is? right = mid - 1 no found, go step 3
step 8: element not found return -1
"""

def binery_search(L, x):
    """ Binary Search"""
    left, right = 0, len(L) - 1

    while left <= right: # position
        mid = (left + right) // 2 # init mid and return int division

        if L[mid] == x:
            return mid

        if L[mid] < x:
            left = mid + 1
        else:
            right = mid - 1

    return -1 


if __name__ == "__main__":
    L = sorted([3,5,6,8,9])

    for x in range(1, 11):
        position = binery_search(L, x)

        if position == -1: # not found
            if x in L:
                print(x, " is in L, but function returned -1")
            else:
                print(x, "not in list")
        else:
            if L[position] == x:
                print(x, "found in correct position.")
            else:
                print("binary  search returned", position, "for", x, "which is incorrect")
    print("program terminated")