import numpy as np
import math


def collatz(n, sequence, count=1, orig=-1):
    sequence.append(n)

    if orig == -1:
        orig = n

    if n == 1:
        return count, sequence

    if n % 2 == 0:
        n /= 2
    else:
        n = 3 * n + 1

    return collatz(n, sequence, count + 1, orig)


def reversecollatz(n, count=1, sequence=[], orig=-1, prevn=-1, node=0, depth=-1, newnode=False):

    depth += 1
    sequence[node].append([prevn, n, count])

    if newnode:
        print("new node # ", node)

    print("inside node.  node # ", node, ".  prevn:  ", prevn,
          ".  n:  ", n, ".  count:  ", count, ".  depth:  ", depth)

    if n > 1e6 or (n <= 1 and n > -100):
        if sequence[node][1][1] != -1:
            print("terminus:  ", node, sequence[node], depth)
            debugpausingvar = 1

        n = -999

        depth -= 1

        return prevn, n, count, sequence[:], depth

    if n == -999:

        depth -= 1
        return prevn, n, count, sequence[:], depth

    if orig == -1:
        orig = n

    if n % 2 == 0:
        prevnodd = -1
        newnodd = -1
        countnewnodd = -1

        # the collatz sequence takes an odd number, multiplies by 3 and adds 1:  n1 = 3 * n0 + 1
        # it takes an even number and divides by 2.  n1 = n0 / 2
        # performing the odd operation in reverse:  n0 = (n1-1)/3.  if n0 was even, this case wouldn't apply as n0 even would use the even operation (n1 = n0 / 2).
        # if n0 were even, i.e. 2m (generic even number).  2m = (n1-1)/3 => n1 = 6m+1.  if n1 is odd, doing the reverse odd operation would give an even.
        # which is an impossible case.  only do the reverse odd operation if n
        # is even.  obviously, aslo if it would result in an integer.

        if (n - 1) / 3 % 1 == 0:
            # consider an odd operation to be a new branch.  even ones are
            # commonplace.
            node += 1
            sequence.append([node])
            # can i return count and test it against current count?
            prevnodd, newnodd, countnewodd, sequence, depth = reversecollatz(
                n=(n - 1) / 3, count=count + 1, sequence=sequence, orig=orig, prevn=n, node=node, depth=depth, newnode=True)
            debugpausingvar = -1
        # can i also return this count and test the two?  is that valid?
        prevneven, newneven, countnewneven, sequence, depth = reversecollatz(
            n=prevn * 2, count=count + 1, sequence=sequence, orig=orig, prevn=n, node=node, depth=depth, newnode=False)
        debugpausingvar = -1

        prevn = prevneven
        n = newneven
        count = countnewneven

        if countnewnodd > countnewneven:
            n = newnodd
            count = countnewnodd
            prevn = prevnodd

    else:
        prevn, n, countdontneed, sequence, depth = reversecollatz(
            n=n * 2, count=count + 1, sequence=sequence, orig=orig, prevn=n, node=node, depth=depth, newnode=False)

    depth -= 1

    return prevn, n, count, sequence[:], depth


n = 8

count = 4

sequence = []

sequence.append([0])

prevn, n, count, sequence, depth = reversecollatz(
    n=n, count=count, sequence=sequence, newnode=False)

print(prevn, n, count)
