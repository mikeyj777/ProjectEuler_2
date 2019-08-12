# The sum of the squares of the first ten natural numbers is,
#
# 12 + 22 + ... + 102 = 385
# The square of the sum of the first ten natural numbers is,
#
# (1 + 2 + ... + 10)2 = 552 = 3025
# Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025 − 385 = 2640.
#
# Find the difference between the sum of the squares of the first one
# hundred natural numbers and the square of the sum.

# sum of nat nums:  Sn = n(n+1)/2
# sum of squares of nat nums:  S2n = n(n+1)(2n+1)/6

import math

n = 10


def sqsumofnats(n):
    return math.pow(n * (n + 1) / 2, 2)


def sumofsqnats(n):
    return n * (n + 1) * (2 * n + 1) / 6


sqsn = sqsumofnats(n)

ssqn = sumofsqnats(n)

diff = sqsn - ssqn

print(sqsn, ssqn, diff)
