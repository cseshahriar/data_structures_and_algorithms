""" Big O notation """

# =============== get order of n ============
# time = a * n + b (linear equation)
# keep fastest growing term rule
# time = a * n
# drop b constants rule
# time = O(n) so time complexity is order of N


def get_squared_numbers(numbers):
    """ function definition """
    return [n*n for n in numbers]


numbers = [2, 5, 8, 9, 9]
result = get_squared_numbers(numbers)
print(result)  # [4, 25, 64, 81]

# =========== get order of 1 O(1) ===========


def find_first_pe(prices, eps, index):
    return prices[index]/eps[index]   # index constant operation


# find duplicates time = a * n^2 + b { O(n^2) }

# n^2 iteration
duplicate = None
for i in range(len(numbers)):
    for j in range(i+1, len(numbers)):
        if numbers[i] == numbers[j]:
            duplicate = numbers[i]
            break

# n iteration
for i in range(len(numbers)):
    if numbers[i] == duplicate:
        duplicate = numbers[i]
        break

print(duplicate)
# time = a * n^2 + b * n + c

# Big O two rules
# 1. keep fastest growing term
# 2. Drop constants

"""
BigO refers to very large value of n. Hence if you have a function like
time = 5 * n^2 + 3*n + 20
When value of n is very large b * n + c become irrevalant

Example : n = 1000
time = 5 * 1000^2 + 3*1000 + 20
time = 5000000 + 3020
"""

# ======================== space complexity ===================
data = [4, 9, 15, 21, 34, 57, 68, 91]  # search 68 O(n) complexity
for i in range(len(data)):
    if data[i] == 68:
        print(i)  # index found 7 iteration

# better way binary search
"""
data = [4, 9, 15, 21, 34, 57, 68, 91]
iteration1 = n / 2
data = [4, 9, 15, 21, 34, 57, 68, 91]  21 is middle

iteration2 = (n / 2) / 2 = n/2^2
data = [34, 57, 68, 91]  57 is middle


iteration3 = (n / 2^2)/2 = n/2^3
data = [68, 91]  68 is middle
found 3 iteration


iteration k = n/2k
1 = n/2k  # worst case
n = 2k
log2 n = log2 2k
log2 n = k * log2 2                 # { [log2 2] = 1 }
K = log n -> O(log n)
k = O(log n) -> log2 8 -> log2 2^3 -> 3 * log2 2 -> 3 iteration
"""
