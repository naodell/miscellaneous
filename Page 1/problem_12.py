'''
    The sequence of triangle numbers is generated by adding the natural
    numbers. So the 7th triangle number would be 1 + 2 + 3 + 4 + 5 + 6 + 7 =
    28. The first ten terms would be:

    1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...

    Let us list the factors of the first seven triangle numbers:

    1: 1
    3: 1,3
    6: 1,2,3,6
    10: 1,2,5,10
    15: 1,3,5,15
    21: 1,3,7,21
    28: 1,2,4,7,14,28

    We can see that 28 is the first triangle number to have over five divisors.

    What is the value of the first triangle number to have over five hundred divisors?

'''

import math

nDivisors   = 0
count       = 2
target      = 0

while(nDivisors < 500):

    triangle = sum(range(count))
    divisors = []

    divisors.append(triangle)

    for n in range(1,int(math.sqrt(triangle))):
        if triangle%n == 0:
            divisors.append(n)
            divisors.append(triangle/n)

    if len(divisors) > nDivisors:
        nDivisors   = len(divisors)
        target      = triangle
        print nDivisors

    count = count + 1
    
print 'The solution is ', target
