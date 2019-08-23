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
from datetime import datetime


def sumofnumsnotsumsofabundants(n):

    #     divisors = np.arange(1, n // 2 + 1)

    abundants = []
    sumsofabundantpairs = []
    temp = []

    t0 = datetime.now()

    for i in range(1, n + 1):
        temp = np.array([m for m in np.arange(1, i // 2 + 1) if i %
                         m == 0 and not m == i])
        y = temp.sum()

        if i % 1000 == 0:
            print(datetime.now() - t0)
            t0 = datetime.now()

        if y > i:
            #             print(i, len(abundants))
            temp = [i + x for x in abundants if x != i]
            abundants.append(i)
            sumsofabundantpairs.extend(temp)
            sumsofabundantpairs = list(dict.fromkeys(sumsofabundantpairs))

    allthenums = range(1, n + 1)

    sumslow = [x for x in sumsofabundantpairs if x <= 28123]
    notapair = [x for x in allthenums if x not in sumslow]

    return sum(notapair)


n = 28123

a = sumofnumsnotsumsofabundants(n)

print(a)
