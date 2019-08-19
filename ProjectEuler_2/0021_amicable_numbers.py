# Let d(n) be defined as the sum of proper divisors of n (numbers less than n which divide evenly into n).
# If d(a) = b and d(b) = a, where a ≠ b, then a and b are an amicable pair and each of a and b are called amicable numbers.
#
# For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110; therefore d(220) = 284. The proper divisors of 284 are 1, 2, 4, 71 and 142; so d(284) = 220.
#
# Evaluate the sum of all the amicable numbers under 10000.


import numpy as np
import math
import itertools


def sumofamicablesbelown(n):

    divisors = np.arange(1, n // 2)

    d = {}

    amicables = []

    for i in range(1, n):
        temp = np.array([m for m in divisors if i % m == 0 and not m == i])
        y = temp.sum()
        d[i] = y
        if y < i and y != 0:
            if d[y] == i:
                amicables.append(y)
                amicables.append(i)

    amicables = np.unique(amicables)

    return amicables.sum()


n = 10000

a = sumofamicablesbelown(n)

print(a)
