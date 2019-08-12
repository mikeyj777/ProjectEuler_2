import math
import numpy as np


def reversecollatz(n, count=2, node=0, sequence=[],
                   depth=0, maxcount=-1, bestruns=[], maxnode=0):

    depth += 1

    sequence[node].append([n, count, depth])

    if n > 1e6 or n == 4:

        if count > maxcount:
            bestrun = sequence[node][len(sequence[node]) - 2]
            print(bestrun)
            bestruns.append(bestrun)
            maxcount = count
        return n, sequence[:], depth, maxcount, bestruns[:], maxnode

    if n % 2 == 0:

        if (n - 1) / 3 % 1 == 0:

            node = maxnode + 1

            maxnode = node

            sequence.append([node, n])

# n, count=2, node=0, sequence=[],
#                    depth=0, maxcount=-1, bestruns=[]

            n, sequence, depth, maxcount, bestruns, maxnode = reversecollatz(
                (n - 1) / 3, count + 1, node,
                sequence, depth, maxcount, bestruns, maxnode)

            n = sequence[node][1]

            node = maxnode + 1
            maxnode = node
            sequence.append([node, n])

    n, sequence, depth, maxcount, bestruns, maxnode = reversecollatz(
        n * 2,  count + 1, node,
        sequence, depth, maxcount, bestruns, maxnode)

    n = sequence[node][1]

    depth -= 1

    return n, sequence[:], depth, maxcount, bestruns[:], maxnode


n = 8
count = 3
node = 0
sequence = []
sequence.append([node, n])

nout, sequence, depth, maxcount, bestruns, maxnode = reversecollatz(
    n, count=count + 1, node=node,
    sequence=sequence, depth=-1, maxcount=-1, bestruns=[], maxnode=node)

print(bestruns)
# bestruns:  n, count, depth
