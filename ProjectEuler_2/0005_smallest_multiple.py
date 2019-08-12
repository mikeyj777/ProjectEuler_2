# 2520 is the smallest number that can be divided by each of the numbers
# from 1 to 10 without any remainder.

# What is the smallest positive number that is evenly divisible by
# all of the numbers from 1 to 20?

# method:
# 1.  generate list of primes below 20
# 2.  generate 2D matrix of prime factors for all numbers 20 and below
# 3.  for each row of matrix (each number up to 20), record the max value of each column
# 4.  the max value of each column is the greatest power of each prime factor needed
# to generate that value.  if the greatest power of each prime factor is tracked,
# then the values comprised by combinations of lower powers are also covered.

import numpy as np
import math


def take3(x, arr, ubound):
    primefactors = []
    n = 0
    while n < arr.shape[0]:
        if x % arr[n] == 0:
            temp = arr[n]
            #x /= arr[n]
            primefactors.append(temp)
            if n < arr.shape[0] - 1:
                arr = np.arange(arr[n + 1], ubound + 1)
            for ellie in primefactors:
                arr = arr[arr[:] % ellie != 0]
            n = -1
        n += 1
    return primefactors


x = 2
for i in range(3, 21):
    x *= i

arr = np.arange(2, 21)

primes = take3(x, arr, 20)


def factorization(value, primes, factors):
    if value == 1:
        return factors
    for prime in primes:
        if value % prime == 0:
            factors[prime] += 1
            value /= prime
            return factorization(value, primes, factors[:])


values = np.zeros((21, 21))
for value in range(values.shape[0]):
    if value > 1:
        factors = np.zeros(21)
        thefactors = factorization(value, primes, factors)
        #print(value, thefactors)
        values[value] = thefactors

print(values)


lm = np.zeros(21)
for value in values:
    for factor in range(value.shape[0]):
        lm[factor] = max(lm[factor], value[factor])

print(lm)

i = 1
index = 0
for factor in lm:
    if factor > 0:
        i *= math.pow(index, factor)
    index += 1
print(i)
