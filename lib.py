import timeit


def run(f):
    print timeit.timeit('print %s()' % f.__name__, 'from __main__ import %s' % f.__name__, number=1)


def split_by_digit(n):
    li = []
    while n > 0:
        li.append(n % 10)
        n /= 10
    return li


def is_prime(x):
    sq = x ** 0.5
    n = 2
    while n <= sq:
        if x % n == 0:
            return False
        n += 1
    return True


def integer_factorization(n):
    primes = [i for i, v in enumerate(prime_sieve(int(n ** 0.5) + 1)) if i > 1 and v]
    return trial_division(n, primes)


def trial_division(n, primes):
    if n == 1: return {}
    prime_factors = {}

    for p in primes:
        if p * p > n: break
        while n % p == 0:
            prime_factors[p] = prime_factors.setdefault(p, 0) + 1
            n //= p
    if n > 1:
        prime_factors[n] = prime_factors.setdefault(n, 0) + 1

    return prime_factors


def prime_sieve(n):
    sieve = [False] * 2 + [True] * (n - 2)
    for i in xrange(2, int(n ** 0.5) + 1):
        if sieve[i]:
            for j in xrange(i * 2, len(sieve), i):
                sieve[j] = False
    return sieve


def sum_of_divisors(n):
    factors = integer_factorization(n)
    sum = 1
    for f in factors:
        sum *= (f ** (factors[f] + 1) - 1) / (f - 1)
    return sum


def is_pandigital(n, digits):
    digits = set([int(i) for i in digits])
    s = str(n)
    for i in range(len(s) - 1):
        for j in range(i + 1, len(s)):
            if s[i] == s[j]:
                return False
    for c in s:
        if int(c) not in digits:
            return False
    return True


def permutation_gen(s):
    if len(s) == 1:
        yield s
    else:
        for i in xrange(len(s)):
            for perm in permutation_gen(s[:i] + s[i + 1:]):
                yield s[i] + perm


def gcd(a, b):
    while b:
        a, b = b, a % b
    return a


def lcm(a, b):
    return a * b // gcd(a, b)
