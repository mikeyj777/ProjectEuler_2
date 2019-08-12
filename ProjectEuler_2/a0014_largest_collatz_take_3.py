import numpy as np
import math
from datetime import datetime


def collatz(n, count=1, store=[]):
    #     print(n)

    if n == 1:

        return count

    if n % 2 == 0:
        return collatz(n / 2, count + 1)
    else:
        return collatz(3 * n + 1, count + 1)

    store.append([n, count])

    return count


def control():
    bestn = -1
    t0 = datetime.now()
    print("start:  ", t0)
    maxcount = -1
    count = []
    for i in range(1, 101):
        count.append([math.pow(2, i), i])
    count = np.array(count)

    for n in range(2, 1000000):
        nums = count[0][:, ]
        ncount = -1
        targappendval = -1
        if n not in nums:
            ncount = collatz(n)
            count = np.concatenate(count, [[n, ncount]])
        else:
            rownum = (count[:, 0] == [n]).nonzero()
            ncount = count[rownum][1]
        if n % 2 == 0 and n / 2 not in nums:
            targappendval = n / 2
        if n % 2 == 1 and 3 * n + 1 not in nums:
            targappendval = 3 * n + 1
        if targappendval > 0:
            count = np.concatenate(count, [[targappendval, ncount + 1]])

        if ncount > maxcount:
            maxcount = count
            bestn = n
            print(n, count)
    tf = datetime.now()
    print("finish:  ", tf, ".  delta:  ", tf - t0)

    return bestn


bestn = control()

print(bestn)


def reversecollatz(n, count=1, buffer=[]):

    buffer[0] = buffer[1]
    buffer[1] = [n, count]

    print(n, count)

    if n == 1 or n == 4:

        buffer = []
        for i in range(2):
            buffer.append([])

        return n, count, buffer[:]

    oddcolltest = (n - 1) / 3

    if oddcolltest % 1 == 0 and oddcolltest % 2 == 1:

        nodd, countodd, buffer = reversecollatz(oddcolltest, count + 1, buffer)
        buffer[1] = [n, count]
    else:
        neven, counteven, buffer = reversecollatz(n * 2, count + 1, buffer)
        buffer[1] = [n, count]

    return n, count, buffer


def reversecontrol():

    n = 837799

    count = 0

    buffer = []

    for i in range(2):
        buffer.append([])

    nout, count, buffer = reversecollatz(n, count, buffer)

    return [nout, count, buffer]


# data = reversecontrol()
#
# print(data)
