import numpy as np
import math

currval = 0

with open('data/proj13input.txt') as f:
    for line in f:
        line = line.strip('\n')
        line = line.strip('\t')
        currval += int(line)


finval = str(currval)

print(finval)
