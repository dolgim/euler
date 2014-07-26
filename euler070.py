import math

from euler import lib


def e70():

    ubound = 10 ** 7

    sieve = lib.prime_sieve(int(ubound ** 0.5) + 1)
    primes = [i for i, v in enumerate(sieve) if i > 1 and v]

    def totient(n):
        _phi = n
        for _p in lib.trial_division(n, primes).keys():
            _phi /= _p
            _phi *= _p - 1
        return _phi

    def permutation_each(n1, n2):
        if int(math.log10(n1)) != int(math.log10(n2)):
            return False
        c = [0] * 10
        while n1 > 0:
            c[n1 % 10] += 1
            n1 /= 10
        while n2 > 0:
            c[n2 % 10] -= 1
            n2 /= 10
        return len(filter(lambda x: x != 0, c)) == 0

    min_value = 10**5
    min_n = 1
    for n in xrange(3, ubound, 2):
        phi = totient(n)
        if (n - phi) % 9 == 0 and permutation_each(n, phi):
            val = float(n) / phi
            if val < min_value:
                min_value = val
                min_n = n
                print n, phi, val

    return min_n


def e71():
    nearest_n = 0
    nearest_d = 1
    for d in xrange(1000001):
        n = d * 3 / 7
        if d % 7 == 0:
            n -= 1
        if lib.gcd(n, d) > 1:
            continue
        if n * nearest_d > d * nearest_n:
            nearest_n = n
            nearest_d = d
    return nearest_n, nearest_d


def e72():
    ubound = 10 ** 6

    sieve = lib.prime_sieve(int(ubound ** 0.5) + 1)
    primes = [i for i, v in enumerate(sieve) if i > 1 and v]

    def totient(n):
        _phi = n
        for _p in lib.trial_division(n, primes).keys():
            _phi /= _p
            _phi *= _p - 1
        return _phi

    count = 0
    for d in xrange(2, ubound + 1):
        count += totient(d)
    return count


def e73():

    count = 0
    for d in xrange(4, 12001):
        l = [n for n in xrange(d / 3 + 1, math.ceil(float(d) / 2)) if lib.gcd(n, d) == 1]
        count += len(l)
    return count


def e74():

    def digit_factorial(n):
        s = 0
        while n > 0:
            s += math.factorial(n % 10)
            n /= 10
        return s

    chain_cache = {}
    count = 0
    for n in xrange(1000000):
        chain = []
        chain_set = set([])
        chain_len = 0
        df = n
        while True:
            if df in chain_cache:
                chain_len = len(chain) + chain_cache[df]
                for i, m in enumerate(chain):
                    chain_cache[m] = chain_len - i
                break
            chain.append(df)
            chain_set.add(df)
            df = digit_factorial(df)
            if df in chain_set:
                idx = chain.index(df)
                chain_len = len(chain)
                for i, m in enumerate(chain):
                    chain_cache[m] = chain_len - min(i, idx)
                break
        #print n, chain_len

        if chain_len == 60:
            count += 1
    return count


def e75():
    l_bound = 1500000
    l_dict = {}

    # for every natural number m, n that n < m
    # primitive pythagorean triple a, b, c = mm - nn, 2mn, mm + nn
    for n in xrange(1, int(l_bound ** 0.5 / 2) + 1):  # m > n & a + b + c <= l ==> n < sqrt(l)/2 < m
        for m in xrange(n + 1, l_bound):
            l = 2 * m * (m + n)
            if l > l_bound:
                break
            if lib.gcd(m, n) != 1 or (m - n) % 2 != 1:
                continue
            l0 = l
            while l0 <= l_bound:
                #print l0/l*(m*m - n*n), l0/l*2*m*n, l0/l*(m*m + n*n), l0
                l_dict[l0] = l0 not in l_dict
                l0 += l
    return len([b for b in l_dict.values() if b])


lib.run(e75)
