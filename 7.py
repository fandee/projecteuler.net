"""
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
"""

import math
from time import time

def is_prime(x):
    sqrt = int(math.sqrt(x))+1
    for i in range(2, sqrt, 1):
        if x % i == 0:
            return False
    return True

t1 = time() # start time

n = 0
i = 0
while n != 10002:
    i += 1
    if is_prime(i):
        n += 1

t2 = time() # end time

print('Answer:', i)
print('Time:', (t2-t1)/1000, 'sec') # 0.0006-0.0007