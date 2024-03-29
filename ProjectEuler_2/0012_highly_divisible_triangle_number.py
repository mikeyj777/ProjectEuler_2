import numpy as np
import math

# The sequence of triangle numbers is generated by adding the natural numbers. So the 7th triangle number would be 1 + 2 + 3 + 4 + 5 + 6 + 7 = 28. The first ten terms would be:
#
# 1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...
#
# Let us list the factors of the first seven triangle numbers:
#
#  1: 1
#  3: 1,3
#  6: 1,2,3,6
# 10: 1,2,5,10
# 15: 1,3,5,15
# 21: 1,3,7,21
# 28: 1,2,4,7,14,28
# We can see that 28 is the first triangle number to have over five divisors.
#
# What is the value of the first triangle number to have over five hundred
# divisors?

# find a number 'a' with 500 primes below it

# calculate Sn = a where Sn = n(n+1)/2

# calculate n from quadratic formula:  n = (-1+sqrt(1+8a)/2)

# round n up and calculate how many divisors it has

# scale 'a' by additional required divisors.

# if number of divisors > 500 return a.


def numberofprimesbelown(n):
    return n / math.log(n)


def numberwithpprimesbelowit(p):
    y1 = 30
    x1 = numberofprimesbelown(y1)
    y2 = 100
    x2 = numberofprimesbelown(y2)
    m = (y2 - y1) / (x2 - x1)
    b = y1 - m * x1

    initguess = m * p + b

    value = numberofprimesbelown(initguess) - p

    x0 = initguess
    x1 = x0 + 1

    while abs(value) > 0.01:
        y0 = numberofprimesbelown(x0) - p
        y1 = numberofprimesbelown(x1) - p

        x2 = x1 - y1 * (x1 - x0) / (y1 - y0)

        x0 = x1
        x1 = x2
        value = numberofprimesbelown(x2) - p

    return x2


def nfromsn(sn):
    n = (-1 + math.sqrt(1 + 8 * sn)) / 2
    return int(n)


def sumofnatnumsbelown(n):
    return n * (n + 1) / 2


def numdivisors(sn):
    totdivisors = 2
    arr = np.arange(2, sn + 1)
    while sn > 1 and arr.shape[0] > 0:
        if sn % arr[0] == 0:
            totdivisors += 1
            sn /= arr[0]
        else:
            arr = arr[arr[:] % arr[0] != 0]
    return totdivisors


def findnumberwithspecifieddivisors(targdivisors, currdivisors, workingvalue):
    if currdivisors >= targdivisors:
        return currdivisors
    a = numberwithpprimesbelowit(workingvalue)
    n = nfromsn(a)
    sn = sumofnatnumsbelown(n)
    currdivisors = numdivisors(sn)
    workingvalue = targdivisors / currdivisors * workingvalue
    print("a:  ", a, ".  n:  ", n, ".  sn:  ", sn, ".  currdivisors:  ",
          currdivisors, ".  workingvalue:  ", workingvalue)
    return findnumberwithspecifieddivisors(targdivisors, currdivisors, workingvalue)


targdivisors = 501
currdivisors = 0
workingvalue = 501

thehightriangle = findnumberwithspecifieddivisors(
    targdivisors, currdivisors, workingvalue)

print(thehightriangle)
