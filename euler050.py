import math

from euler import lib
import prime


e50_l = 1000000


def e50():
    sieve = lib.prime_sieve(e50_l)
    primes = [i for i, n in enumerate(sieve) if n]
    primes_count = len(primes)
    m = (0, 0, 0)
    for i in xrange(primes_count):
        s, c = primes[i], 1
        for j in xrange(i + 1, primes_count):
            c += 1
            s += primes[j]
            if s >= e50_l:
                break
            if sieve[s]:
                if m[0] < c:
                    m = (c, s, i)
                    #print primes[i:j+1], (c, s, i)
                    #print m[0:2]
    return m


def e50_1():
    sieve = lib.prime_sieve(e50_l)
    primes = [i for i, n in enumerate(sieve) if n]
    primes_count = len(primes)
    prime_sum = primes[0]
    left = 0
    right = 1
    for i in xrange(primes_count):
        s = sum(primes[i:right])
        if sum(primes[i:i + right - left]) > e50_l:
            break
        if i == right:
            print '???'
            break
        for j in xrange(right, primes_count):
            if s + primes[j] >= e50_l:
                break
            s += primes[j]
            if sieve[s]:
                if right - left < j - i + 1:
                    prime_sum = s
                    left = i
                    right = j + 1
                    #print m, s, sum(primes[i:j+1]), primes[i:j+1]

    return prime_sum, left, right


def e51():
    max_digit = 6
    sieve = lib.prime_sieve(10 ** max_digit)

    fmts = {}

    for i in range(max_digit):
        fmts[i] = {}
        for j in range(2, max_digit - i + 1):
            fmts[i][j] = [fmt.replace('x', '%s') for fmt in set(list(lib.permutation_gen('x' * i + '*' * j)))]

    for x in xrange(10 ** (max_digit - 1)):
        s = str(x)
        l = len(s)
        for i in range(2, max_digit - l + 1):
            for fmt in fmts[l][i]:
                fmt = fmt % tuple(s)
                nums = [int(fmt.replace('*', str(t))) for t in range(1 if fmt.startswith('*') else 0, 10)]
                prime_count = len(filter(lambda u: sieve[u], nums))
                if prime_count >= 8:
                    return fmt, nums


def e52():
    def same_digit(a, b):
        a, b = list(str(a)), list(str(b))
        a.sort()
        b.sort()
        if len(a) != len(b):
            return False
        for i in range(len(a)):
            if a[i] != b[i]:
                return False
        return True

    maxnum = 1000000
    for n in xrange(1, maxnum / 6):
        if all([same_digit(n, (i + 1) * n) for i in range(1, 6)]):
            return n


def e53():
    total = 0
    for n in range(1, 101):
        denom, numer = 1, 1
        for r in range(1, n / 2 + 1):
            denom *= n - r + 1
            numer *= r
            if denom / numer > 1000000:
                print n, r, denom / numer, n - r - r + 1
                total += n - r - r + 1
                break
    return total


def e54():
    rank_key = ['high card', 'one pair', 'two pairs', 'three of a kind', 'straight', 'flush', 'full house', 'four of a kind',
                'straight flush', 'royal flush']
    rank_value = dict((v, k) for k, v in enumerate(rank_key))

    def fmt(st):
        for i in range(2, 10):
            st = st.replace(str(i), '0' + str(i))
        for i, j in {'T': '10', 'J': '11', 'Q': '12', 'K': '13', 'A': '14'}.iteritems():
            st = st.replace(i, j)
        return st

    def rank(cards):
        r = 0
        flush = len(set([c[2:] for c in cards])) == 1

        dic = {}
        for c in cards:
            v = c[:2]
            dic[v] = dic.get(v, 0) + 1
        order = []
        o = {}
        for k, v in dic.iteritems():
            kl = o.get(v, [])
            kl.append(k)
            o[v] = kl
        for k in sorted(o.iterkeys(), reverse=True):
            order += sorted(o[k], reverse=True)
        l = len(dic)

        if l == 5:
            if int(cards[-1][:2]) - int(cards[0][:2]) + 1 == 5:
                r = rank_value['straight']
                if flush:
                    r = rank_value['straight_flush']
                    if cards[-1][:2] == fmt('A'):
                        r = rank_value['royal_flush']
        elif flush:
            r = rank_value['flush']
        elif l == 2:
            if max(dic) == 4:
                r = rank_value['four of a kind']
            else:
                r = rank_value['full house']
        elif l == 3:
            if max(dic) == 3:
                r = rank_value['three of a kind']
            else:
                r = rank_value['two pairs']
        elif l == 4:
            r = rank_value['one pair']

        return r, order

    with open('euler054.in', 'r') as f:
        loop = 0
        win_count = 0
        for line in f.readlines():
            line = line.strip()
            li = fmt(line.strip()).split(' ')
            rank_a, rank_b = rank(sorted(li[:5])), rank(sorted(li[5:]))
            if rank_a[0] > rank_b[0]:
                winner = 'A'
            elif rank_a[0] < rank_b[0]:
                winner = 'B'
            else:
                i = 0
                while rank_a[1][i] == rank_b[1][i]:
                    i += 1
                    if i >= len(rank_a):
                        break
                winner = 'A' if rank_a[1][i] > rank_b[1][i] else 'B'

            if winner == 'A':
                win_count += 1
            loop += 1
            if rank_a[1] == rank_b[1]:
                break
            if rank_a[0] != 0 and rank_b[0] != 0:
                continue
            if rank_a[1][0] != '14' and rank_b[1][0] != '14':
                continue
            if rank_a[1][1] != '05' and rank_b[1][1] != '05':
                continue
            print 'Round %d: %s wins.' % (loop, winner)
            print ' '.join(sorted(line.split(' ')[:5])), '(%15s)' % rank_key[rank_a[0]], ','.join(rank_a[1])
            print ' '.join(sorted(line.split(' ')[5:])), '(%15s)' % rank_key[rank_b[0]], ','.join(rank_b[1])

        return loop, win_count


def e55():

    def is_palindromic(n):
        return n == int(str(n)[::-1])

    count = 0
    for n in xrange(10000):
        s = n
        is_lychrel = True
        for i in xrange(50):
            s += int(str(s)[::-1])
            if is_palindromic(s):
                is_lychrel = False
                break
        if is_lychrel:
            count += 1
            print n
    return count


def e56():

    max_sum = 0
    for a in range(2, 100):
        for b in range(1, 100):
            s = sum(map(int, list(str(a ** b))))
            if max_sum < s:
                max_sum = s
    return max_sum


def e57():
    a = [(2, 1)]
    count = 0
    for n in xrange(1000):
        denom, numer = a[n][1], a[n][0]
        denom += numer * 2
        a.append((denom, numer))
        if int(math.log10(denom + numer)) > int(math.log10(denom)):
            count += 1
            print (denom + numer, denom)
    return count


def e58():

    maxnum = 20000
    prime_count = 0
    count = 1
    for n in xrange(2, maxnum):
        count += 4
        x = (2 * n - 1) ** 2
        for m in range(1, 4):
            if prime.isprime(x - 2 * (n - 1) * m):
                prime_count += 1
        ratio = float(prime_count) / count
        if ratio <= 0.1:
            print 2 * n - 1, prime_count, '/', count, '=', ratio
            break


def e59():
    def r():
        return range(ord('a'), ord('z') + 1)
    with open('euler059.in') as f:
        cipher = eval('[' + f.read() + ']')
        for l in r():
            for m in r():
                for n in r():
                    key = (l, m, n)
                    original = []
                    valid = True
                    for i, char in enumerate(cipher):
                        c = char ^ key[i % 3]
                        if 32 <= c < 127:
                            original.append(c)
                        else:
                            valid = False
                            break
                    if valid:
                        original_str = ''.join(map(chr, original))
                        if original_str.find('the') == -1 or original_str.find('The') == -1:
                            continue
                        print ''.join(map(chr, key)), original_str.find('the'), original_str
                        print sum(original)



lib.run(e59)