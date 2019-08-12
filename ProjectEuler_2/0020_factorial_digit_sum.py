# n! means n × (n − 1) × ... × 3 × 2 × 1
#
# For example, 10! = 10 × 9 × ... × 3 × 2 × 1 = 3628800,
# and the sum of the digits in the number 10! is 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.
#
# Find the sum of the digits in the number 100!

# used code from power digit sum.  changed '2' to 'm' in temp = ans[i] * m
# + carry

import numpy as np


def mult():
    carry = 0
    ans = np.zeros(1000)
    numdigits = 1
    currpos = ans.shape[0] - 1
    ans[ans.shape[0] - 1] = 1

    for m in range(2, 101):

        getout = False
        for i in range(ans.shape[0] - 1, -1, -1):
            #             if getout:
            #                 break
            temp = ans[i] * m + carry
            carry = 0
            ans[i] = temp % 10
            if temp >= 10:
                carry = (temp - temp % 10) / 10
    print(ans)
    print(np.sum(ans))


mult()
