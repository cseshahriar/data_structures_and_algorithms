"""
input: A list , n elements 
step 1: i name var and value 0 to (n - 1) before increse by one,
        i every value go step 2

step 2: L[i+1] and L[i-1] find smallest element index that el index
        element swap
step 3: list elements sorted smallest to bigest 
"""
def selection_sort(L):
    """ Selection Soft"""
    n = len(L) # list length

    for i in range(0, n-1): # start 0 to stop list length
        index_main = i # current index position

        for j in range(i+1, n): # next el to list length
            if L[j] < L[index_main]: # list[j] if less than list[current index position or upper loop]
                index_main = j

        if index_main != i:
            L[i], L[index_main] = L[index_main], L[i] # swap


if __name__ == '__main__':
    L = [6, 1, 4, 9, 2]
    print("Before soft:", L)
    selection_sort(L)
    print("After soft:", L)