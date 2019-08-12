import numpy as np
import math

# A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
#
# a2 + b2 = c2
# For example, 32 + 42 = 9 + 16 = 25 = 52.
#
# There exists exactly one Pythagorean triplet for which a + b + c = 1000.
# Find the product abc.


def c(b):
    return (1000000 - 2000 * b + 2 * b**2) / (2000 - 2 * b)


def a(b, ccalc):
    return math.sqrt(ccalc**2 - b**2)


solns = []

for b in range(1, 999):
    ctest = c(b)
    atest = a(b, ctest)

    if atest % 1 == 0 and ctest % 1 == 0 and atest > 0 and ctest > 0 and atest < 999 and ctest < 999:
        solns.append((atest, b, ctest))

solns = np.array(solns)

print(solns)

for soln in solns:
    testpyth = soln[0] ** 2 + soln[1] ** 2 - soln[2]**2
    testsum = soln[0] + soln[1] + soln[2]
    print("python triple test (should be zero):  ", testpyth)
    print("sum test (should be 1000):  ", testsum)

soln = solns[0]

prod = 1
for val in soln:
    prod *= val

print(prod)
