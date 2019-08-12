import numpy as np

# 2^15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.

# What is the sum of the digits of the number 2^1000?


def mult():
    carry = 0
    ans = np.zeros(1000)
    currpow = 9
    seed = 2**currpow
    numdigits = 3
    currpos = ans.shape[0] - 1
    ans[ans.shape[0] - 1] = 2
    ans[ans.shape[0] - 2] = 1
    ans[ans.shape[0] - 3] = 5

    for m in range(10, 1001):

        getout = False
        for i in range(ans.shape[0] - 1, -1, -1):
            #             if getout:
            #                 break
            temp = ans[i] * 2 + carry
            carry = 0
            ans[i] = temp % 10
            if temp >= 10:
                carry = (temp - temp % 10) / 10
#             if ans.shape[0] - i > numdigits:
#                 numdigits += 1
#                 getout = True
    print(ans)
    print(np.sum(ans))


mult()
