"""
Fibonacci
first, second fibo is 1,1
odl two number summation 
if n = 4 then 2 + 3 = 5
"""
def fibonacci(n):
    if n in [1, 2]:
        return 1

    return fibonacci(n - 2) + fibonacci(n - 1) # formula

def test_fibonacci():
    fibo = [1,1,2,3,5,8,13,21,34,55,89]
    for n, f in enumerate(fibo):
        print('n , f', n, f)
        assert fibonacci(n+1) == f