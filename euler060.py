import itertools
import operator
import math

import lib
import prime


def e60():

    def concat(m, n):
        return m * (10 ** int(math.log10(n) + 1)) + n

    def is_prime(n):
        return prime.isprime(n)

    def is_concatenatable(m, n):
        return is_prime(concat(m, n)) and is_prime(concat(n, m))

    def find_sol(below):
        below = 50000
        primes = []

        doubles = {}
        triples = {}
        quadruples = {}
        quintuples = {}

        tuples = ({}, {}, doubles, triples, quadruples, quintuples)

        for p in prime.primes_below(below):
            if p % 100 < 10:
                print p
            if below < p:
                break
            li = []
            print p
            for q in primes:
                if p <= q:
                    break
                if is_concatenatable(p, q):
                    # print p, q
                    doubles[p * q] = (q, p)
                    li.append(q)
            print li
            for r in range(2, min(len(li), 5)):
                for t in itertools.combinations(li, r):
                    x = reduce(operator.mul, t)
                    if x not in tuples[r]:
                        continue
                    tuples[r + 1][p * x] = t + tuple([p])
                    if r < 4:
                        continue

                    # First quintuple
                    min_sum = sum(t) + p

                    for tp in quadruples.values():
                        tp_sum = sum(tp)
                        print tp, '(sum=%d): from %d to %d' % (tp_sum, p, min_sum - tp_sum)
                        for p0 in prime.primes_above(p):
                            if tp_sum + p0 > min_sum:
                                break
                            if all([is_concatenatable(p0, p1) for p1 in tp]):
                                min_sum = tp_sum + p0

                    return min_sum
            primes.append(p)
    return find_sol(50000)


def e61():

    def l(f):
        li = []
        n = 0
        while True:
            n += 1
            x = f(n)
            if x < 1000: continue
            if x > 10000: break
            li.append(x)
        return li

    tris = l(lambda n: n * (n + 1) / 2)
    sqrs = l(lambda n: n * n)
    pentas = l(lambda n: n * (3 * n - 1) / 2)
    hexas = l(lambda n: n * (2 * n - 1))
    heptas = l(lambda n: n * (5 * n - 3) / 2)
    octas = l(lambda n: n * (3 * n - 2))

    nums = [tris, sqrs, pentas, hexas, heptas, octas]

    def find_next(sol):
        seq = [x[0] for x in sol]
        last_index, last = sol[-1]
        last %= 100
        for i in range(6):
            if i in seq:
                continue
            for j in range(len(nums[i])):
                if nums[i][j] / 100 == last:
                    yield (i, nums[i][j])

    def find_all(sol):
        if len(sol) == 6:
            if sol[-1][1] % 100 == sol[0][1] / 100:
                return True
            return False
        count = 0
        for i, n in find_next(sol):
            count += 1
            sol.append((i, n))
            print_solution(sol)
            if find_all(sol):
                return True
            else:
                sol.pop()
                print_solution(sol)
        if count == 0:
            return False

    def print_solution(sol):
        pass
        #print '=>'.join(['%d(%d)' % (n, i) for i, n in sol])

    solution = [None]
    for t in nums[0]:
        solution[0] = (0, t)
        if find_all(solution):
            break
    print solution
    return sum([t[1] for t in solution])


def e62():

    def key(n):
        return ''.join(sorted(str(n)))

    bucket = {}

    n = 1
    while True:
        c = n * n * n
        h = key(c)
        if h not in bucket:
            bucket[h] = []
        bucket[h].append(c)
        if len(bucket[h]) == 5:
            return min(bucket[h])
        n += 1


def e63():
    a = 1
    count = 0
    while True:
        li = [b for b in range(9, 0, -1) if 10 ** (a - 1) <= b ** a]
        c = len(li)
        print a, li, map(lambda b: b ** a, li)
        if c == 0:
            break
        count += c
        a += 1
    return count


def e64():
    limit = 10000
    count = 0
    for n in xrange(2, limit + 1):
        sq_n = n ** 0.5
        li = []
        a, b, c = (int(sq_n), int(sq_n), 1)
        if int(sq_n + 0.5) ** 2 == n:
            continue
        while True:
            c = (n - b * b) / c
            a = int((sq_n + b) / c)
            b = c * a - b
            if len(li) > 0 and li[0] == (a, b, c):
                if len(li) % 2 == 1:
                    count += 1
                break
            li.append((a, b, c))
            a, b, c = li[-1]

    return count


def e65():

    def convergent(n):

        def a(k):
            if k % 3 == 2:
                return (k + 1) / 3 * 2
            else:
                return 1

        def convergent_inner(m):
            if m == 0:
                return 0, 1
            if m == 1:
                return a(n), 1
            numer, denom = convergent_inner(m - 1)
            return a(n - m + 1) * numer + denom, numer

        num, den = convergent_inner(n)
        return 2 * num + den, num

    print sum([int(s) for s in str(convergent(99)[0])])


def e66():

    def cont_frac_sq(x):
        sq_x = x ** 0.5
        li = []
        if int(sq_x + 0.5) ** 2 == x:
            return [int(sq_x)]
        a, b, c = (int(sq_x), int(sq_x), 1)
        while True:
            c = (x - b * b) / c
            a = int((sq_x + b) / c)
            b = c * a - b
            if len(li) > 0 and li[0] == (a, b, c):
                break
            li.append((a, b, c))
            a, b, c = li[-1]
        return [int(sq_x)] + [t[0] for t in li]

    def convergent_sq(li, n):

        def convergent_inner_denom(m):
            if m == 0:
                return 1, li[n]
            numer, denom = convergent_inner_denom(m - 1)
            return denom, li[n - m] * denom + numer

        if n == 0:
            return li[0], 1
        if len(li) == 1:
            return n, 1
        if n > len(li):
            li *= int(math.ceil(float(n) / len(li)))
        num, den = convergent_inner_denom(n-1)
        return den, li[0] * den + num

    def pell_first_sol(x):
        li = cont_frac_sq(x)
        if len(li) == 1:
            return None
        r = len(li) - 2
        if r % 2 == 1:
            k = r
        else:
            k = 2 * r + 1
        return convergent_sq(li, k)

    def is_square(n):
        return n > 0 and (round(n ** 0.5) ** 2 == n)

    max_x = 0
    max_d = 0
    for d in xrange(2, 1000):
        if is_square(d):
            continue
        y, x = pell_first_sol(d)
        if x > max_x:
            max_x = x
            max_d = d
            print d, x, y
    return max_d


def e67():
    def print_triangle(tri):
        for v in tri:
            print v

    with open('euler067.in', 'r') as f:
        tri = [[int(n) for n in line.split(' ')] for line in f]

        for y in xrange(len(tri)-2, -1, -1):
            for x in xrange(len(tri[y])):
                tri[y][x] += max(tri[y+1][x: x+2])

    print tri[0][0]


def e68():

    sieve = [False] * 11
    int_node = []
    ext_node = []

    def mark(n):
        sieve[n] = True

    def unmark(n):
        sieve[n] = False

    def marked(n):
        return sieve[n]

    def gen(n):
        for m in range(max(1, n-10), min(n/2 + 1, 10)):
            if m == n - m:
                continue
            if marked(m) or marked(n - m):
                continue
            #print n, m, n - m
            mark(m)
            mark(n - m)
            yield m, n - m
            yield n - m, m
            unmark(m)
            unmark(n - m)

    max_sol = 0

    a = 10
    mark(a)
    for s in range(14, 20):
        for f, g in gen(s - a):
            for j, e in gen(s - f):
                for i, d in gen(s - j):
                    for h, c in gen(s - i):
                        b = s - h - g
                        if 0 < b < 10 and not marked(b):
                            ext_node = [a, b, c, d, e]
                            int_node = [f, g, h, i, j]
                            min_idx = ext_node.index(min(ext_node))
                            ext_node = ext_node[min_idx:] + ext_node[:min_idx]
                            int_node = int_node[min_idx:] + int_node[:min_idx]
                            print ext_node, int_node
                            li = []
                            for x in range(5):
                                li += [ext_node[x], int_node[x], int_node[(x+1) % 5]]
                            sol = int(''.join([str(x) for x in li]))
                            if sol > max_sol:
                                max_sol = sol
    return max_sol


def e69():

    below = 1000000
    max_n = 1
    max_ratio = 0

    # Fastest way: using n/phi(n) = PI(p|n, p / p - 1), all p have to be smallest as possible to maximum n/phi
    m = 1
    for n in prime.primes_above(1):
        if m * n > below:
            return m
        m *= n

    # Brute force
    for n in xrange(2, below):
        phi = n
        for p in lib.integer_factorization(n).keys():
            phi /= p
            phi *= p - 1
        #print n, phi
        ratio = 1.0 * n / phi
        if ratio > max_ratio:
            max_n = n
            max_ratio = ratio

    return max_n

#profile.run('e60()')

lib.run(e60)

