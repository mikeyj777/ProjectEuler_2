import numpy as np

import csv

import math

from datetime import datetime

from scipy.io.matlab.miobase import arr_dtype_number

from collections import Counter


def primesbelown(n):

    primes = []

    arr = np.zeros(n // 2 + 1)

    arr[0] = 2

    arr[1:] = np.arange(3, n + 1, 2)

    while arr.shape[0] > 0:

        if n % arr[0]:

            primes.append(arr[0])

        arr = arr[arr[:] % arr[0] != 0]

        primes = np.array(primes)

        return primes


# print(primesbelown(56495217870))


def numberofprimesbelown(n):

    return n / math.log(n)


def firstnprimes(n):

    primes = []

    primes.append(2)

    p = 3

    count = 1

    while count < n:

        numisprime = False

        while not numisprime:

            numisprime = True

            for prime in primes:

                if p % prime == 0:

                    numisprime = False

                    break

            if numisprime:

                primes.append(p)

                count += 1

            p += 2

    return primes


def getnextprime(primes=[]):

    if len(primes) == 0 or max(primes) == 1:
        return 2

    if max(primes) == 2:
        return 3

    p = max(primes) + 2

    numisprime = False

    while not numisprime:

        numisprime = True

        for prime in primes:

            if p % prime == 0:

                numisprime = False

                break

        if numisprime:
            break

        if max(primes) % 2 != 0:
            p += 2
        else:
            p += 1

    return p


def ncr(n, r):

    return math.factorial(n) / math.factorial(n - r) / math.factorial(r)


def numberwithpprimesbelowit(p):

    y1 = 30

    x1 = numberofprimesbelown(y1)

    y2 = 100

    x2 = numberofprimesbelown(y2)

    m = (y2 - y1) / (x2 - x1)

    b = y1 - m * x1

    initguess = m * p + b

    value = numberofprimesbelown(initguess) - p

    x0 = initguess

    x1 = x0 + 1

    while abs(value) > 0.01:

        y0 = numberofprimesbelown(x0) - p

        y1 = numberofprimesbelown(x1) - p

        x2 = x1 - y1 * (x1 - x0) / (y1 - y0)

        x0 = x1

        x1 = x2

        value = numberofprimesbelown(x2) - p

    return x2


def nfromsn(sn):

    n = (-1 + math.sqrt(1 + 8 * sn)) / 2

    return n


def istriangular(sn):
    n = (-1 + math.sqrt(1 + 8 * sn)) / 2
    return n % 1 == 0


def npnfromsn(sn):

    n = (-1 + np.sqrt(1 + 8 * sn)) / 2

    return n


def nfromsnisinteger(sn):

    if nfromsn(sn) % 1 == 0:

        return True

    return False


def sumofnatnumsbelown(n):

    return n * (n + 1) / 2


def npr(n, r):

    return math.factorial(n) / math.factorial(n - r)


def permuteutil(sstr, count, result, level, resultlist=[]):

    if (level == len(result)):

        resultlist.append(result[:])

        return None

    for i in range(len(sstr)):

        if (count[i] == 0):

            continue

        result[level] = sstr[i]

        count[i] -= 1

        permuteutil(sstr, count, result, level + 1, resultlist)

        count[i] += 1


def permute(sstr, count, result, level, resultlist=[]):

    if (level == len(result)):

        resultlist.append(result[:])

#         print(count, result[:])

        return resultlist

    for i in range(len(sstr)):

        if (count[i] == 0):

            continue

        result[level] = sstr[i]

        count[i] -= 1

        resultlist = permute(sstr, count, result, level + 1, resultlist)

        count[i] += 1

    return resultlist


def permuteandtest(sstr, count, result, level, primes, r, resultlist=[], minanswer=-1, summer=[], allresults=[]):

    if (level == len(result)):

        #         print(result)

        thesum = np.sum(np.array(result))

        summer.append(thesum)

        if thesum == r:

            answer = np.power(primes, result)

            answer = np.prod(answer)

            nval = nfromsn(answer)

            if nval % 1 == 0:

                alltheprimes = []
                prime = -1
                for r in result:
                    prime += 1
                    for rin in range(r):
                        alltheprimes.append(primes[prime])

                numdivs = numdivisors(primes=alltheprimes)

                if numdivs > 500:

                    if minanswer == -1:

                        minanswer = answer

                    if answer < minanswer:

                        minanswer = answer

                    allresults.append(result[:])

                    print("answer:  ", answer, "minanswer:  ", minanswer)

        return resultlist

    for i in range(len(sstr)):

        if (count[i] == 0):

            continue

        result[level] = sstr[i]

        count[i] -= 1

        resultlist = permuteandtest(
            sstr, count, result, level + 1, primes, r, resultlist, minanswer, summer, allresults)

        count[i] += 1

    return resultlist


def printallrows(arr):

    for row in arr:

        print(row)

    return None


def writetocsv(arr, name=''):

    arr = np.array(arr)

    name += '_' + str(datetime.now())

    name = name.replace(':', '_')

    name = name.replace('-', '_')

    name = name.replace(' ', '_')

    if name[-4:] != '.csv':

        name = name.replace('.', '_')

        name = name + '.csv'

    if name[:5] != 'data/':

        name = 'data/' + name

    np.savetxt(name, arr, delimiter=',')

    return None


def allpermutsoflist(sstr):

    count = []

    result = []

    for i in range(len(sstr)):

        count.append(1)

    prods = []

    for i in range(1, len(sstr) + 1):

        result = []

        for n in range(1, i + 1):

            result.append(0)

        resultlist = permute(sstr, count, result, 0)

        for currset in resultlist:

            prod = 1

#             print(currset)

            for num in currset:

                prod *= num

            prods.append(prod)

    return np.unique(prods)


def primefactors(n):

    primes = primesbelown(n)

    orig = n

    primefacts = []

    for i in range(len(primes)):

        if n % primes[i] == 0:

            primefacts.append(primes[i])

            n /= primes[i]

            i -= 1

    return primefacts


def divisorsandnumdivisors(n=-1, primes=[], r=-1):

    # provide either n or primes

    if len(primes) == 0:

        primes = primefactors(n)

    divs = []

    divs.append(1)

    for prime in primes:

        divs.append(prime)

    if n > 0:

        divs.append(n)

    divs = allcombos(divs, r)

    divs = np.array(divs)

    maxval = n

    if maxval < 0:

        maxval = 1

        for prime in primes:

            maxval *= prime

    divs = divs[divs[:] <= maxval]

    return divs, divs.shape[0]


def numdivisors(n=-1, primes=[], r=-1):

    divs, numdivs = divisorsandnumdivisors(n, primes, r)

    return numdivs


def divisorsonly(n=-1, primes=[], r=-1):

    divs, numdivs = divisorsandnumdivisors(n, primes, r)

    return divs


#     arr[]  ---> Input Array

#    data[] ---> Temporary array to store current combination

#    start & end ---> Starting and Ending indexes in arr[]

#    index  ---> Current index in data[]

#    r ---> Size of a combination to be printed


def combinations(arr, data, start, end, index, r, combos=[]):

    #      Current combination is ready to be printed, print it

    if (index == r):

        combos.append(data[:])

#         print("combo: ", data)

        return combos[:]


#     replace index with all possible elements. The condition

# end-i+1 >= r-index" makes sure that including one element

# at index will make a combination with remaining elements

# at remaining positions

    for i in range(start, end):

        if end - i + 1 >= r - index:

            data[index] = arr[i]

            combos = combinations(

                arr, data, i + 1, end, index + 1, r, combos[:])

    return combos


def allcombos(sstr, r=-1):

    rmaxnoti = True

    if r == -1:

        rmaxnoti = False

    result = []

    prods = []

    for i in range(1, len(sstr) + 1):

        result = []

        for n in range(1, i + 1):

            if rmaxnoti and n > r:

                break

            result = []

            for m in range(n):

                result.append(0)

            resultlist = combinations(sstr, result, 0, i, 0, n)

            for currset in resultlist:

                prod = 1

#                 print(currset)

                for num in currset:

                    prod *= num

                prods.append(prod)

    return np.unique(prods)


def findhightrinum():

    maxdivs = 0

    divparams = []

    writeheader = True

    n = 2079

    looping = True

    t0 = datetime.now()

    while looping:

        sn = sumofnatnumsbelown(n)

        _, numdivs = divisorsandnumdivisors(sn)

    #     print(numdivs)

        if numdivs > maxdivs:

            if numdivs > 500:

                looping = False

                print(datetime.now() - t0)

            maxdivs = numdivs

            divparams.append([n, sn, numdivs, maxdivs])

            with open('data/nvsnumdivs.csv', mode='a') as csv_file:

                fieldnames = ['n', 'sn', 'numdivs', 'maxdivs']

                writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

                if writeheader:

                    writer.writeheader()

                    writeheader = False

                writer.writerow({'n': n,

                                 'sn': sn,

                                 'numdivs': numdivs,

                                 'maxdivs': maxdivs})

        print(n, sn, numdivs, maxdivs)

        n += 1

    print("end")

    return None


# Print all members of ar[] that have given

def findNumbers(ar, sum, i, res=[], r=[]):

    # If  current sum becomes negative

    if sum < 0:

        return None

    # if we get exact answer

    if sum == 0:

        res.append(r[:])

        return res

    # Recur for all remaining elements that

    # have value smaller than sum.

    while (i < len(ar) and sum - ar[i] >= 0):

         # Till every element in the array starting

         # from i which can contribute to the sum

        r.append(ar[i])

        # recur for next numbers

        res = findNumbers(ar, sum - ar[i], i, res, r)

        i += 1

        # remove number from list (backtracking)

        r.pop()

    return res


# Returns all combinations of ar[] that have given

# sum.

def combinationSum(ar, sum):

    # sort input array

    ar.sort

    # remove duplicates

    ar = list(dict.fromkeys(ar))

    res = findNumbers(ar, sum, 0)

    return res


def gettotalsofeachnum(ar, sum):

    res = []

    res = combinationSum(ar, sum)

    counts = []

    for r in res:

        countdict = Counter(r)

        count = []

        for i in range(len(ar) + 1):
            count.append(0)

        for key, value in countdict.items():
            if key <= sum:
                count[key] = value
            else:
                print("stopper")

#         print(count)

        counts.append(count)

    return counts


def tester():

    ar = [1, 2, 3, 4, 5]

    # for i in range(ar):

    #    n.append(0)

    sum = 5  # set value of sum

    res = combinationSum(ar, sum)

    return res


def usencrtofindhightri():

    n = 0

    keeplooping = True

    answers = []

    while keeplooping:

        n += 1

        primes = np.array(firstnprimes(n))

        primes = np.flip(primes)

        result = []

        for i in range(n):

            result.append(0)

        for r in range(1, n + 1):

            #             if ncr(n, r) > 500:

            if ncr(n, r) > 500:

                print("npr: ", npr(n, r))

                print("ncr: ", ncr(n, r))

                if ncr(n, r) == 715.0:
                    print("stopper")

                inputnums = np.arange(r + 1)
                inputnumsnozero = np.arange(1, r + 1)
                counts = gettotalsofeachnum(inputnumsnozero, r)

                for count in counts:

                    count[0] = n - r + count.count(0) - 1

                    exponentpermutations = np.array(permuteandtest(
                        inputnums, count, result, 0, primes, r, [], -1,))

                    if exponentpermutations.shape[0] > 0:

                        print("primes: ", primes)

                        print("exponents: ", exponentpermutations)

                        primeraisedtopermutation = np.power(
                            primes, exponentpermutations)

                        print("primeraisedtopermutation: ",
                              primeraisedtopermutation)

                        prods = np.prod(primeraisedtopermutation, axis=1)

                        nsfromsn = npnfromsn(prods)

                        nsfromsn = nsfromsn[nsfromsn[:] % 1 == 0]

                        if nsfromsn.shape[0] > 0:

                            divs = np.apply_along_axis(
                                func1d=numdivisors, axis=0, arr=prods)

                            if divs.shape != ():

                                prods = prods[divs[:] > 500]

                                answers.append(np.min(prods))

    return None


def incrementprimecombinations(primes=[2], exponents=[1]):
    primes = [2]
    exponents = [1]

    currval = np.prod(np.power(primes, exponents))

    if istriangular(currval):
        expincr = np.array(exponents) + 1
        if np.prod(expincr) > 500:
            return currval

    keeplooping = True

    while keeplooping:

        newvals = []
        for i in range(len(exponents)):
            exponents[i] += 1
            a = np.prod(np.power(primes, exponents))
            newvals.append([i, a])
            exponents[i] -= 1
            minval = newvals[0]
            for newval in newvals:
                if newval[1] < minval[1]:
                    minval = newval
            newval1 = minval

        a = getnextprime(primes)
        primes.append(a)
        exponents.append(1)

        newval2 = np.prod(np.power(primes, exponents))

        newval = -1
        if newval1[1] < newval2:
            exponents[newval1[0]] += 1
            newval = newval1[1]
            primes.pop()
            exponents.pop()
        else:
            newval = newval2

        if istriangular(newval):
            expincr = np.array(exponents) + 1
            if np.prod(expincr) > 500:
                return newval


# incrementprimecombinations()

def testingdivs():

    keeplooping = True
    primes = [2]
    answers = []
    while keeplooping:
        expprod = 1
        for prime in primes:
            prod = prime
            for exponent in range(len(primes)):
                expprod *= exponent
                a = math.pow(prime, exponent)
                prod *= a
                print("prime: ", prime, "exponent: ", exponent,
                      "prime**exponent: ", a, "prod: ", prod, "expprod: ", expprod)

                if expprod > 500:
                    if istriangular(prod):
                        print(prod, " works!")
                        answers.append(prod)

        primes.append(getnextprime(primes))

    return answers


# testingdivs()


def integersqrt(n):
    x = n
    y = (x + 1) // 2
    while y < x:
        x = y
        y = (x + n // x) // 2
    return x


def useintegersqrttodetermineifnumistriangular(sn):
    discriminant = integersqrt(1 + 8 * sn)
    n = (-1 + discriminant) / 2

    return n * (n + 1) / 2 == sn


def testingdivs2():

    n = 500

    primes = primefactors(n)

    print("primes:  ", primes)

    divs1, numdivs1 = divisorsandnumdivisors(n=n)

    divs2, numdivs2 = divisorsandnumdivisors(primes=primes)

    print("n-based:  ", divs1, numdivs1)

    print("primes-based:  ", divs2, numdivs2)

    return None


def testingdivs3():

    # all numbers can be written as composites of primes, each to a given exponent
    # number of divisors = products of each (exponent + 1)
    # add a prime.
    # try all permutations of the primes and powers up to that number of primes
    # check which value is triangular and has divisors > 500
    # this took ~2 min to find a matching result, so it doesn't technically qualify
    # also, I don't know a way to definitively say that this answer is the best.
    # only by entering each returned value until one of them was correct was I
    # able to consider this solved

    minval = -1

    keeplooping = True

    primes = []

    answers = []

    while keeplooping:

        primes.append(getnextprime(primes))

        sstr = []

        count = []

        result = []

        for i in range(len(primes)):
            sstr.append(i)

            count.append(len(primes))

            result.append(0)

        exponentslist = permute(sstr, count, result, 0, [])

        for exponents in exponentslist:
            ans = np.prod(np.power(primes, exponents))

            numdivs = 1

            for exponent in exponents:
                numdivs *= (exponent + 1)

#             print(ans, numdivs)

            if ans > 0 and numdivs > 500 and useintegersqrttodetermineifnumistriangular(ans):
                if minval == -1:
                    minval = ans
                    answers.append(ans)
                    print(ans)
                else:
                    if ans < minval:
                        minval = ans
                        print(ans)
                        answers.append(ans)
                        if len(answers) % 10 == 0:
                            print(answers)
                            print()

    return None


testingdivs3()
