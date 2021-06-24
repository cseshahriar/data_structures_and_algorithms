"""
Bubble Sort:
step 1: i 0 to n increse by one and process step 2
step 2: j 0 to (n - i - 1) increase by one and process step 3
step 3: if list[j] > list[j+1] is, then swap
step 4: sorted list
"""

def bubble_soft(L):
    """ Bubble sort """
    n = len(L) # list length

    for i in range(0, n): # step 1 (iterate 0 to n-1) means for the L 0 to 4(5-1)
        for j in range(0, n-i-1): # step 2
            if L[j] > L[j+1]: # step 3
                L[j], L[j+1] = L[j+1], L[j] # swap

if __name__ == "__main__":
    L = [6, 1, 4, 9, 2]
    print("Before sort", L)
    bubble_soft(L)
    print("After sort", L)
