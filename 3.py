'''
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
'''

import math

def is_prime(x):
    sqrt = int(math.sqrt(x))+1
    for i in range(2, sqrt, 1):
        if x % i == 0:
            return False
    return True

n = 600851475143
if n <= 1:
    exit() 
_max = 0

while not is_prime(n):
    for i in range(2, n, 1):
        if n % i == 0:
            print(i)
            n = int(n / i)
            _max = i if i > _max and is_prime(i) else _max
            break
_max = n if n > _max else _max

print(_max)