# A perfect number is a number for which the sum of its proper divisors is exactly equal to the number. For example, the sum of the proper divisors of 28 would be 1 + 2 + 4 + 7 + 14 = 28, which means that 28 is a perfect number.
#
# A number n is called deficient if the sum of its proper divisors is less than n and it is called abundant if this sum exceeds n.
#
# As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16, the smallest number that can be written as the sum of two abundant numbers is 24. By mathematical analysis, it can be shown that all integers greater than 28123 can be written as the sum of two abundant numbers. However, this upper limit cannot be reduced any further by analysis even though it is known that the greatest number that cannot be expressed as the sum of two abundant numbers is less than this limit.
#
# Find the sum of all the positive integers which cannot be written as the
# sum of two abundant numbers.


import numpy as np
import math
import itertools


def sumofnumsnotsumsofabundants(n):

    divisors = np.arange(1, n // 2)

    d = {}

    abundants = []

    for i in range(1, n):
        temp = np.array([m for m in divisors if i % m == 0 and not m == i])
        y = temp.sum()
        d[i] = y
        if y > i:
            abundants.append(i)

    abundantsums = []

    for i in abundants:
        for n in abundants:
            if n != i:
                abundantsums.append(i + n)

    allthenums = range(1, n + 1)

    return sum(list(set(allthenums) - set(abundantsums)))


n = 28123

a = sumofnumsnotsumsofabundants(n)

print(a)
