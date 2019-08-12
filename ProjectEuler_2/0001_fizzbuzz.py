# If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
# Find the sum of all the multiples of 3 or 5 below 1000.

# method:
# the multiples of 3 below 1000 are 3,6,9,...,999.  These can be rewritten as
# 3(1+2+3+...+333).  This is 3 x the sum of natural numbers up to 333.
# This factor will be called "Sn(3,999)"
#
# The formula for sum of first n natural numbers is:
# Sn = n(n+1)/2
#
# This same methodology will be used to sum the numbers below 1000 divisible
# by 5.  n here would be 199 (5 * 199 = 995, last multiple of 5 less than 1000).
# This factor will be called "Sn(5,995)"
#
# The sum of multiples of 3 below 1000 ("Sn(3,999)") plus the sum of multiples of 5
# below 1000 ("Sn(5,995)")will get us almost there.  this method will double-count multiples of 15, we will subtract the sum of
# multiples of 15 up to 990 (n = 990/15 = 66)
# This factor will be called  "Sn(15,990)".
#
#  sum of all the multiples of 3 or 5 below 1000
#     = 3 * Sn(3,999) + 5 * Sn(5,995) - 15 * Sn(15,990)
#     = 233168.0


def numofmultiplesofxbelowy(x, y):
    return (y - 1) // x


def s(n):
    return n * (n + 1) / 2


s3 = s(numofmultiplesofxbelowy(3, 1000))
s5 = s(numofmultiplesofxbelowy(5, 1000))
s15 = s(numofmultiplesofxbelowy(15, 1000))

answer = 3 * s3 + 5 * s5 - 15 * s15
print(answer)
