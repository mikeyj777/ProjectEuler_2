import numpy as np
import math

ubound = 2e6


def totalofprimes(ubound):
    arr = np.arange(2, ubound + 1)
    tot = 0
    count = 0
    while arr.shape[0] > 0:
        count += 1
        if count % 1000 == 0:
            print(arr[0], tot)
        tot += arr[0]
        arr = arr[arr[:] % arr[0] != 0]
    return tot


print(totalofprimes(ubound))
