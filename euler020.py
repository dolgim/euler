import math

from euler import lib


def e20():
    return reduce(lambda x, y: int(x) + int(y), list(str(math.factorial(100))))


def e21():
    max = 10000
    primes = [i for i, n in enumerate(lib.prime_sieve(int(max ** 0.5) + 1)) if i > 1 and n]
    li = [0] * max

    for n in xrange(1, max):
        sum = lib.sum_of_divisors(n) - n
        li[n] = sum

    sum = 0
    for n in xrange(1, max):
        m = li[n]
        if n != m and m < max and li[m] == n:
            print n, m
            sum += n

    return sum


def e22():
    with open('euler022.in', 'r') as f:
        total = 0
        li = eval('[' + f.read() + ']')
        li.sort()
        for i, v in enumerate(li):
            total += sum(map(lambda x: ord(x) - 64, v)) * (i + 1)
        return total


def e23():
    rng = 28123
    abundants = []
    for n in xrange(1, rng):
        s = lib.sum_of_divisors(n)
        if s - n > n:
            abundants.append(n)

    print len(abundants)

    sums = set()
    l = len(abundants)
    for i in xrange(l):
        for j in xrange(i, l):
            s = abundants[i] + abundants[j]
            if s < rng:
                sums.add(s)
            else:
                break

    sum = 0
    for n in xrange(l):
        if n not in sums: sum += n

    return sum


def e24():
    x = 1000000
    p = ''
    e = range(0, 10)
    x -= 1
    for i in range(len(e) - 1, -1, -1):
        n = math.factorial(i)
        j = x / n
        d = e[j]
        e.remove(d)
        p += str(d)
        x -= n * j
    #		print p, n, d, n*d, x, e
    return p


def e25():
    a = 1
    b = 1
    i = 3
    t = 10 ** 999
    while i < 10000:
        f = a + b
        b = a
        a = f
        if f >= t:
            print i, f
            break
        i += 1


def e26():
    longest_cycle = (1, 0)
    for n in range(2, 1000):
        m = n
        while m != 0 and m % 5 == 0:
            m %= 5
        while m != 0 and m % 2 == 0:
            m %= 2
        if m == 0:
            continue
        cycle = 0
        for k in xrange(1, n):
            if 10 ** k - 1 == 10 ** k / n * n:
                cycle = k
                break
        if longest_cycle[1] < cycle:
            longest_cycle = (n, cycle)

    print longest_cycle


def e27():
    l = 1000
    maxnum = (0, 0, 0)
    for a in xrange(-l + 1, l):
        for b in xrange(-l + 1, l):
            n = 0
            while lib.is_prime(n * n + a * n + b):
                n += 1
            if n > maxnum[2]:
                maxnum = (a, b, n)

    print maxnum, maxnum[0] * maxnum[1]


def e28():
    s = 1
    for n in xrange(1, 500 + 1):
        s += 4 * (2 * n + 1) ** 2 - 12 * n
    return s


def e29():
    terms = set()
    for a in xrange(2, 101):
        for b in xrange(2, 101):
            terms.add(a ** b)

    return len(terms)

print e23()