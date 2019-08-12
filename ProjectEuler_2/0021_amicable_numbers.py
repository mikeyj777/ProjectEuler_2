import numpy as np
import math


def getprimesbelown(n):
    primes = np.arange(2, n)
    primes = primes[primes[:] % primes[0] != 0]
    return primes


def primefactorizationdict(num, factdict):

    facts = np.arange(2, int(num))
    currfact = 2
    while num > 1:
        if num % facts[0] != 0:
            facts = facts[facts[:] % facts[0] != 0]
        else:
            if currfact == facts[0]:
                if facts[0] in factdict:
                    factdict[facts[0]] += 1
                else:
                    factdict[facts[0]] = 1
            num /= facts[0]

            currfact = facts[0]

    return factdict


factdict = {}

print(primefactorizationdict(2**3 * 5**4, factdict))
