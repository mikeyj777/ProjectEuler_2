import numpy as np
import math

# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
#
# What is the 10 001st prime number?

# 1. estimate size of prime with eqn:  num primes below val ~ value / ln(value)

numprimes = 10001


def upperlimit(primes):
    tol = 0.01

    p = 100000

    pupper = 1000000
    plower = 0

    target = primes
    guess = (pupper + plower) / 2
    calced = guess / math.log(guess)
    while abs(target - calced) / target > tol:
        if calced < target:
            plower = guess
        else:
            pupper = guess
        guess = (pupper + plower) / 2
        calced = guess / math.log(guess)
        print(guess, calced)
    return guess


ubound = (upperlimit(numprimes))

arr = np.arange(2, ubound + 1)

print("arr made")

primefactors = []


def findprimes(arr, primefactors):
    while arr.shape[0] > 0:
        primefactors.append(arr[0])
        arr = arr[arr[:] % arr[0] != 0]
    return primefactors


theprimes = []

while len(theprimes) < numprimes:
    theprimes = findprimes(arr, primefactors)
    if len(theprimes) < numprimes:
        oldubound = ubound
        ubound = ubound * int(numprimes / len(theprimes))
        print(len(theprimes))
        arr = np.arange(oldubound, ubound + 1)
        for prime in theprimes:
            arr = arr[arr[:] % prime != 0]
        print(ubound)
        print("arr made")

print(len(theprimes))
for i in range(5):
    print(theprimes[i])
print(theprimes[10000])
