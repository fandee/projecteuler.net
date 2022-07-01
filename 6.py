'''
The sum of the squares of the first ten natural numbers is 385,

The square of the sum of the first ten natural numbers is 3025,

Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 2640.

Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.
'''
x = 100

sum1 = 0
for i in range(1, x+1):
    sum1 += i**2

sum2 = 0
for i in range(1, x+1):
    sum2 += i
sum2 = sum2**2
print(sum2-sum1)