from math import ceil

def prime_factors(natural_number):
    factors = []

    for x in range(2, ceil(natural_number**.5)+1):
        while natural_number % x == 0:
            natural_number = natural_number/x
            factors.append(x)

    #Some natural numbers will complete the loop with one large prime factor remaining

    if natural_number > 1:
        factors.append(natural_number)

    return factors