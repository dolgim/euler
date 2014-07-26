# -*- coding: utf-8 -*-
from euler import lib


def e40():
    pivots = [0, 1] # starting point by incrementing digit
    for n in range(1, 6):
        pivots.append(pivots[-1] + (10 ** n - 10 ** (n - 1)) * n)

    #pivots[1] = 1
    print pivots
    product = 1

    for n in range(7):
        d = 10 ** n
        for i in range(len(pivots) - 1):
            if pivots[i] <= d and pivots[i + 1] > d:
                pos = d - pivots[i]
                m = pos / i
                x = int(str(10 ** (i - 1) + m)[pos % i])
                print '%d <= %d < %d,' % (pivots[i], d, pivots[i + 1]), pos, m, pos % i, 10 ** (i - 1) + m - 1, x
                product *= x

    return product


def e41():
    for d in range(9, 0, -1):
        if sum(range(d + 1)) % 3 == 0:
            continue
        digits = ''.join(map(lambda d: str(d), range(d, 0, -1)))
        sieve = lib.prime_sieve(int(digits) + 1)
        for p in lib.permutation_gen(digits):
            if sieve[int(p)]:
                print p
                break
        break


def e42():
    trinums = set()
    for i in xrange(1, 50):
        trinums.add(i * (i + 1) / 2)

    triwords = []
    with open('euler042.in', 'r') as f:
        li = eval('[' + f.read() + ']')
        for name in li:
            v = sum([ord(a) - 64 for a in list(name)])
            if v in trinums:
                triwords.append(name)

    print len(triwords)


def e43():
    def method1():
        primes = [2, 3, 5, 7, 11, 13, 17]
        s = ''.join([str(n) for n in range(10)])
        result = 0
        for p in lib.permutation_gen(s):
            divisible = True
            for i in xrange(6, 0, -1):
                if int(p[i + 1:i + 4]) % primes[i] != 0:
                    divisible = False
                    break
            if divisible:
                print p
                result += int(p)

    primes = [2, 3, 5, 7, 11, 13, 17]

    def substr_divisible_gen(curr_str, divisor):
        digits = set([str(t) for t in range(10)]) - set(list(curr_str))
        if len(digits) == 1:
            yield digits.pop() + curr_str
            return
        for d in digits:
            x = d + curr_str[:2]
            if int(x) % divisor != 0:
                continue
            next_str = d + curr_str
            #		print next_str
            try:
                next_divisor = primes[-len(curr_str)]
            except IndexError:
                next_divisor = 1
            for s in substr_divisible_gen(next_str, next_divisor):
                yield s

    def method2():
        digits = set(range(10))
        result = 0
        for i in range(100):
            x = '%02d' % i
            if x[0] == x[1]:
                continue
            for s in substr_divisible_gen(x, primes[-1]):
                print s
                result += int(s)
        print result

    method2()


def e44():
    pentanums = [0]
    l = 2500
    for n in xrange(1, l):
        pentanums.append(n * (3 * n - 1) / 2)
    pentaset = set(pentanums)

    for j in xrange(1, l - 1):
        for k in xrange(j + 1, l):
            p1, p2 = pentanums[j], pentanums[k]
            if p1 + p2 in pentaset and p2 - p1 in pentaset:
                print j, k, p1, p2, p2 - p1
                return


def e45():
    def tri(n):
        return (n * n + n) / 2

    def inv_tri(n):
        return int(round((1.0 / 4 + 2 * n) ** 0.5 - 0.5))

    def penta(n):
        return (3 * n * n - n) / 2

    def inv_penta(n):
        return int(round(((1.0 / 4 + 6 * n) ** 0.5 + 0.5) / 3))

    def is_penta(n):
        return penta(inv_penta(n)) == n

    def hexa(n):
        return (2 * n * n - n)

    def inv_hexa(n):
        return int(round(((1 + 8 * n) ** 0.5 + 1) / 4))

    def is_hexa(n):
        return hexa(inv_hexa(n)) == n

    for n in xrange(286, 100000):
        tn = tri(n)
        if is_penta(tn) and is_hexa(tn):
            print n, tn


def e46():
    sieve = lib.prime_sieve(10000)
    double_squares = {2 * i * i: i for i in xrange(100)}
    for c, is_prime in enumerate(sieve):
        if is_prime or c < 2: continue
        if c % 2 == 0: continue
        goldbach = False
        for p, b in enumerate(sieve[:c]):
            if not b: continue
            if double_squares.has_key(c - p):
                ds = double_squares[c - p]
                #			print '%d = %d - 2*%d^2'%(c, p, ds)
                goldbach = True
                break
        if not goldbach:
            print c
            break


def e47():
    l = 4
    fact = lib.integer_factorization
    factors = []
    for n in xrange(100000, 200000):
        facs = set([p ** e for p, e in fact(n).iteritems()])
        if len(facs) != l:
            factors = []
            continue
        consecutive = True
        slice_index = 0
        for i, s in enumerate(factors):
            if not s.isdisjoint(facs):
                consecutive = False
                slice_index = i
        if not consecutive:
            factors = factors[slice_index + 1:]
        factors.append(facs)
        if len(factors) == l:
            print [reduce(lambda x, y: x * y, s) for s in factors]
            return n - l + 1


def e48():
    return sum([(n**n) % (10**10) for n in xrange(1, 1001)]) % 10 ** 10


def e49():
    l = 10000
    sieve = lib.prime_sieve(l)
    for a in xrange(1000, l):
        if not sieve[a]:
            continue
        st = set([int(x) for x in lib.permutation_gen(str(a)) if int(x) > a])
        li = list(st)
        for c in li:
            b = (a + c) / 2
            if b not in st:
                continue
            if sieve[a] and sieve[b] and sieve[c]:
                print str(a) + str(b) + str(c)

print e49()