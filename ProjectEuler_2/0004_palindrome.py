# Find the largest palindrome made from the product of two 3-digit
# numbers.
#
# method:
# largest mistake was creating a permutating function to get all combos of 3-digit
# numbers.  could have just iterated from 100 to 999.
#
# generate products of 3-digit numbers.  document highest value.

import numpy as np
import csv
import math

sstr = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
count = [3, 3, 3, 3, 3, 3, 3, 3, 3, 3]

resultlist = []
result = [0, 0, 0]


def permuteUtil(sstr, count, result, level):
    if (level == len(result)):
        resultlist.append(result[:])
        return None

    for i in range(len(sstr)):
        if (count[i] == 0):
            continue
        result[level] = sstr[i]
        count[i] -= 1
        permuteUtil(sstr, count, result, level + 1)
        count[i] += 1


permuteUtil(sstr, count, result, 0)

resultlist = np.array(resultlist)

palindromes = []


def getdigfromxatplacea(x, a):
    b = int(x / math.pow(10, a))
    return b % 10


i = len(resultlist)
while i > 0:
    i -= 1
    a = resultlist[i]
    num1 = 100 * a[0] + 10 * a[1] + a[2]
    if num1 < 100:
        continue
    j = len(resultlist)
    while j > 0:
        j -= 1
        b = resultlist[j]
        num2 = 100 * b[0] + 10 * b[1] + b[2]
        if num2 < 100:
            continue
        prod = num1 * num2
        if prod == 906609:
            print(num1, num2, prod)
        mag = int(math.log10(prod))
        himag = mag
        ispalindrome = True
        for lowmag in range(mag):
            if lowmag >= himag:
                break
            lowdig = getdigfromxatplacea(prod, himag)
            hidig = getdigfromxatplacea(prod, lowmag)
            if lowdig != hidig:
                ispalindrome = False
                break
            himag -= 1
        if ispalindrome:
            # print(prod)
            palindromes.append(prod)


palindromes = np.array(palindromes)

print('largest palindrome from product of 2 3-digit numbers: ', np.max(palindromes))
print('number of palindromes ', palindromes.shape[0])
