# If the numbers 1 to 5 are written out in words: one, two, three, four, five, then there
# are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.
#
# If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words,
# how many letters would be used?
#
#
# NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and forty-two)
# contains 23 letters and 115 (one hundred and fifteen) contains 20 letters.
# The use of "and" when writing out numbers is in compliance with British
# usage.

import numpy
import math


class Numnamedict:

    def __init__(self):

        self.thedict = {
            1: "one",
            2: "two",
            3: "three",
            4: "four",
            5: "five",
            6: "six",
            7: "seven",
            8: "eight",
            9: "nine",
            10: "ten",
            11: "eleven",
            12: "twelve",
            13: "thirteen",
            14: "fourteen",
            15: "fifteen",
            16: "sixteen",
            17: "seventeen",
            18: "eighteen",
            19: "nineteen",
            20: "twenty",
            30: "thirty",
            40: "forty",
            50: "fifty",
            60: "sixty",
            70: "seventy",
            80: "eighty",
            90: "ninety",
            100: "hundred"
        }


def givenumbername(num):

    theword = ''

    namesdict = Numnamedict().thedict

    'start at left (msd) and work to right (zeros place)'
    remainder = num
    for i in range(int(math.log10(num)), -1, -1):
        if i == 2:
            hundreds = int(num / 100)
            remainder = num - hundreds * 100
            theword += namesdict[hundreds] + ' hundred '
            if remainder > 0:
                theword += 'and '
            else:
                return theword[:-1]
        if i == 1:
            tens = int(remainder / 10)
            if tens == 1 or tens == 0:
                theword += namesdict[remainder]
                return theword
            else:
                remainder = remainder - tens * 10
                theword += namesdict[tens * 10] + ' '
                if remainder == 0:
                    return theword[:-1]
        if i == 0:
            theword += namesdict[remainder] + ' '

    return theword[:-1]


def counterandsummer():
    totstr = ''
    for i in range(1, 1000):
        totstr += (givenumbername(i))

    charcount = len(totstr) - totstr.count(' ') + len('onethousand')
    return charcount


a = counterandsummer()

print(a)
