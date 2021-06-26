""" if list almost sorted, then it's usually """
def insertion_sort(L):
    n = len(L) # list length

    for i in range(1, n):
        # L[i] is make item assign 
        item = L[i] # right position

        # now for item right place search
        j = i - 1 # left postion

        while j >= 0 and L[j] > item: # item right and L[j] right
            # L[j] to place j+1
            L[j+1] = L[j]
            j = j - 1
            # L[j+1] is right place for item
            L[j+1] = item


if __name__ == '__main__':
    L = [6, 1, 4, 9, 2]
    print('Before sort:', L)
    insertion_sort(L)
    print('After sort:', L)