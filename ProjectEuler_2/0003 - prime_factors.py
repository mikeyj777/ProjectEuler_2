# The prime factors of 13195 are 5, 7, 13 and 29.
#
# What is the largest prime factor of the number 600851475143 ?

import numpy as np
import math
from datetime import datetime

# check if a[n] is prime

x = 600851475143
x = 18052676403000
x = 9999999999999

#x = 9000000000

t0 = datetime.now()


def justtheprimes(a):

    primes = []
    keeplooping = True
    doublebreakout = False
    while keeplooping:
        for n in a:
            if x % n != 0:
                a = a[a[:] != n]
                #print(n, " not divisible.  ")
                break
            else:
                if n not in primes:
                    nprime = True
                    for i in a:
                        if i >= n:
                            break
                        if n != i and n % i == 0:
                            a = a[a[:] != n]
                            #print(n, " not prime.")
                            # print(a)
                            nprime = False
                            break

                    m = n
                    if nprime:
                        primes.append(n)
                        m = 2 * n
                    while m <= np.max(a):
                        a = a[a[:] != m]
                        #print(m, " multiple of prime factor ", n)
                        # print(a)
                        m += n
                    break
        if n >= np.max(a):
            keeplooping = False

    return a


def primelookahead(a):
    #print("x = ", x)
    keeplooping = True
    while keeplooping:
        for i in range(np.alen(a)):
            if x % a[i] != 0:
                #print(a[i], "does not divide ", x)
                a = a[a[:] != a[i]]
                break
            for j in range(i + 1, np.alen(a)):
                if a[i] != a[j] and a[j] % a[i] == 0:
                    a = a[a[:] != a[j]]
                    # print(a)
                    break
        if i >= np.alen(a):
            keeplooping = False
    return a


def take3(x, arr, ubound):
    primefactors = []
    n = 0
    while n < arr.shape[0]:
        if x % arr[n] == 0:
            #x /= arr[n]
            primefactors.append(arr[n])
            arr = np.arange(arr[n + 1], ubound + 1)
            arr = arr[arr[:] % arr[n] != 0]
            n = -1
        n += 1
    return primefactors


l = int(math.sqrt(x))
maxpossans = 1

a = np.arange(2, l + 1)

primefactors = take3(x, a, l)

print(primefactors)
