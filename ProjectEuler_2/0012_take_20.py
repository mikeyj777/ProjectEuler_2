import numpy as np
import math
from util import getnextprime, useintegersqrttodetermineifnumistriangular, permute


def testingdivs3():

    # all numbers can be written as composites of primes, each to a given exponent
    # number of divisors = products of each (exponent + 1)
    # add a prime.
    # try all permutations of the primes and powers up to that number of primes
    # check which value is triangular and has divisors > 500
    # this took ~2 min to find a matching result, so it doesn't technically qualify
    # also, I don't know a way to definitively say that this answer is the best.
    # only by entering each returned value until one of them was correct was I
    # able to consider this solved

    minval = -1

    keeplooping = True

    primes = []

    answers = []

    while keeplooping:

        primes.append(getnextprime(primes))

        sstr = []

        count = []

        result = []

        for i in range(len(primes)):
            sstr.append(i)

            count.append(len(primes))

            result.append(0)

        exponentslist = permute(sstr, count, result, 0, [])

        for exponents in exponentslist:
            ans = np.prod(np.power(primes, exponents))

            numdivs = 1

            for exponent in exponents:
                numdivs *= (exponent + 1)

#             print(ans, numdivs)

            if ans > 0 and numdivs > 500 and useintegersqrttodetermineifnumistriangular(ans):
                if minval == -1:
                    minval = ans
                    answers.append(ans)
                    print(ans)
                else:
                    if ans < minval:
                        minval = ans
                        print(ans)
                        answers.append(ans)
                        if len(answers) % 10 == 0:
                            print(answers)
                            print()

    return None


testingdivs3()
