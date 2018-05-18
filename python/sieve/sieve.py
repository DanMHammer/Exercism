def sieve(limit):

    primes = [x for x in range(2, limit+1)]

    for x in range(2, limit):
        for y in range(2, limit):
            try:
                primes.remove(x*y)
            except(ValueError):
                continue

    return primes
