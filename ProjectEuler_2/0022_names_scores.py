# Using names.txt (right click and 'Save Link/Target As...'), a 46K text file containing over five-thousand first names, begin by sorting it into alphabetical order. Then working out the alphabetical value for each name, multiply this value by its alphabetical position in the list to obtain a name score.
#
# For example, when the list is sorted into alphabetical order, COLIN, which is worth 3 + 15 + 12 + 9 + 14 = 53, is the 938th name in the list. So, COLIN would obtain a score of 938 × 53 = 49714.
#
# What is the total of all the name scores in the file?

import numpy as np

names = np.genfromtxt('data/0022.txt', dtype='str', delimiter=',')
names = np.char.replace(names, '\"', '')
names = np.sort(names)
indices = np.flatnonzero(names) + 1
asciis = np.array([[ord(y) - 64 for y in x] for x in names])
length = max(map(len, asciis))
y = np.array([xi + [None] * (length - len(xi)) for xi in asciis])
y[y == None] = 0
sums = y.sum(axis=1)
asciiprods = np.multiply(indices, sums)
asciiprodsums = asciiprods.sum()
print(asciiprodsums)
