import numpy as np


requestedprimes = int(input("how many prime numbers? "))


def findfirstNprimes(totprimes):
    primefactors = []
    primefactors.append(2)
    n = 2
    while len(primefactors) < totprimes:
        n += 1
        nprime = True
        for a in primefactors:
            if n % a == 0:
                nprime = False
                break
        if nprime:
            primefactors.append(n)

    primefactors = np.array(primefactors)

    return primefactors


print(findfirstNprimes(requestedprimes))
