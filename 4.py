'''
A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.
'''

def is_palindrome(x):
    x = str(x)
    _x = x[::-1]
    if x == _x:
        return True
    return False

max_palindrome = 0
for i in range(100, 1000, 1):
    for j in range(i, 1000, 1):
        val = i * j
        if is_palindrome(val):
            max_palindrome = val if val > max_palindrome else max_palindrome

print('max:', max_palindrome)