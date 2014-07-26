import math

from euler import lib


def e30():
    def digit_list(n):
        return map(lambda x: int(x), list(str(n)))

    s = 0
    for x in xrange(2, 6 * 9 ** 5 + 1):
        if sum(map(lambda x: x ** 5, digit_list(x))) == x:
            print x
            s += x
    return s


def e31():
    def combination(value, coins):
        if value == 0:
            return 1
        if len(coins) == 0:
            return 0
        spliced = list(coins)
        m = max(spliced)
        spliced.pop(spliced.index(m))
        c = combination(value, spliced)
        if m <= value:
            c += combination(value - m, coins)
        return c

    return combination(200, [1, 2, 5, 10, 20, 50, 100, 200])


def e32():
    def pandigital_gen(digit, member=range(1, 10)):
        for n in range(10 ** (digit - 1), 10 ** digit):
            li = []
            m = n
            for d in range(digit):
                x = m % 10
                if x not in member:
                    break
                li.append(x)
                m = m / 10
            if len(li) != digit:
                continue
            if len(set(li)) == digit:
                yield n

    def split_by_digit(n):
        li = []
        while n > 0:
            li.append(n % 10)
            n /= 10
        return li

    pandigitals = set()
    member = set(range(1, 10))
    for digit_a, digit_b in [(2, 3), (1, 4)]:
        for p in pandigital_gen(digit_a, member):
            x = p
            m2 = set(member)
            while x > 0:
                m2.remove(x % 10)
                x /= 10
            for q in pandigital_gen(digit_b, m2):
                x = q
                m3 = set(m2)
                while x > 0:
                    m3.remove(x % 10)
                    x /= 10
                if p * q >= 10 ** (len(member) - digit_a - digit_b):
                    continue
                if set(split_by_digit(p * q)) == m3:
                    print (p, q, p * q)
                    pandigitals.add(p * q)

    print pandigitals, sum(pandigitals)


def e33():
    import fractions

    num, denom = 1, 1
    for y in range(10, 100):
        for x in range(y + 1, 100):
            xx = (x % 10, x / 10)
            yy = (y % 10, y / 10)
            if xx[0] == yy[0] and xx[0] == 0: continue
            for p in range(2):
                for q in range(2):
                    x1, x2 = xx[p], xx[p - 1]
                    y1, y2 = yy[q], yy[q - 1]
                    if x1 != y1 or x2 == 0:
                        continue
                    if x1 == y1 and y2 * 1.0 / x2 == y * 1.0 / x:
                        print y, '/', x, '=', y2, '/', x2, '=', y * 1.0 / x
                        num *= x2
                        denom *= y2
    return num / fractions.gcd(num, denom)


def e34():
    def factorial_sum_by_digit(n):
        s = 0
        while n > 0:
            s += math.factorial(n % 10)
            n /= 10
        return s

    nine_fact = math.factorial(9)

    result = []
    for n in xrange(3, 10000000):
        if n > (int(math.log10(n)) + 1) * nine_fact:
            print n, (int(math.log10(n)) + 1) * nine_fact, 'exit!'
            break
        digit_fact_sum = factorial_sum_by_digit(n)
        if n == digit_fact_sum:
            result.append(n)

    print result, sum(result)


def e35():
    sieve = lib.prime_sieve(1000000)
    circular_primes = set()

    for n in xrange(2, len(sieve)):
        if not sieve[n] or n in circular_primes:
            continue
        c = int(math.log10(n))
        is_cp = True
        for d in range(c + 1):
            n = (n % 10 ** c) * 10 + n / 10 ** c
            if not sieve[n]:
                is_cp = False
                break
        if is_cp:
            for d in range(c + 1):
                n = (n % 10 ** c) * 10 + n / 10 ** c
                circular_primes.add(n)

    return len(circular_primes)


def e36():
    def is_palindrome(str):
        for i in range(len(str) / 2):
            if str[i] != str[-1 - i]:
                return False
        return True

    l = 1000000
    result = 0

    for n in range(1, 10 ** (int(math.log10(l)) / 2)) + ['']:
        for center in range(10) + ['']:
            s = str(n)
            try:
                palin = int(s + str(center) + s[::-1])
            except ValueError:
                continue
            if palin > l:
                continue
            b = bin(palin)[2:]
            if is_palindrome(b):
                print palin, b
                result += palin

    #for n in xrange(l):
    #	if is_palindrome(str(n)) and is_palindrome(bin(n)[2:]):
    #		result += n
    #		print n, bin(n)

    return result


def e37():
    sieve = lib.prime_sieve(1000000)
    result = 0
    for n, p in enumerate(sieve):
        if not p: continue
        m = n
        is_tp = True
        while True:
            m %= 10 ** int(math.log10(m))
            if not sieve[m]:
                is_tp = False
                break
            if m < 10:
                break
        if not sieve[m]:
            is_tp = False
        if not is_tp:
            continue
        m = n
        while m / 10 > 0:
            m /= 10
            if not sieve[m]:
                is_tp = False
                break
        if is_tp:
            result += n
            print n
    print result


def e38():
    def is_unconcatnatable(s, mul, n):
        if len(s) == 0:
            return True
        if int(s) == mul:
            return False
        s2 = str(mul * n)
        if s.find(s2) != 0:
            return False
        return is_unconcatnatable(s[len(s2):], mul, n + 1)

    for pan in lib.permutation_gen('987654321'):
        for i in range(1, 10):
            mul = int(pan[:i])
            if is_unconcatnatable(pan, mul, 1):
                print pan, mul
                return


def e39():
    squares = {x * x: x for x in range(1000)}
    counts = {}
    for x in xrange(1, 1000):
        for y in xrange(1, 1000):
            sqs = x * x + y * y
            if sqs in squares:
                z = squares[sqs]
                sum = x + y + z
                if sum > 1000:
                    break
                li = counts.get(sum, []);
                li.append((x, y, z))
                counts[sum] = li
    result = (0, 0)
    for p in counts:
        if result[1] < len(counts[p]):
            result = (p, len(counts[p]))
    return result