from math import gcd

def primitive_triplets(number_in_triplet, upper_limit = None):
    if number_in_triplet % 4 != 0:
        raise ValueError("Number must be divisible by 4!")
    b = number_in_triplet
    triples = set()
    for m in range(2, b):
        n = b / (2 * m)
        if n >= m:
            pass

        else:
            try:
                a = round(m**2 - n**2)
                c = round(m**2 + n**2)
                if upper_limit and c > upper_limit:
                    pass
                elif gcd(c, gcd(a, b)) != 1 or a**2 + b**2 != c**2:
                    pass
                else:
                    x = sorted([a,b,c])
                    triples.add((x[0], x[1], x[2]))
            except TypeError:
                pass
    return triples


def triplets_in_range(range_start, range_end):
    triples = set()
    triples_multiply = set()
    triples_out = set()

    for b in range(range_start, range_end + 1):
        try:
            triples.update(primitive_triplets(b, range_end))
        except ValueError:
            pass

    for elem in triples:
        a, b, c = elem
        for x in range(1, round(range_end/b)+1):
            triples_multiply.add((a*x, b*x, c*x))

    """for elem in triples_multiply:
        a, b, c = elem
        if a >= range_start and c <= range_end:
            triples_out.add((a, b, c))"""

    return triples_multiply


def is_triplet(triplet):
    if len(triplet) != 3:
        raise ValueError("Triplet must have exactly 3 elements.")
    triplet = sorted(triplet)
    a, b, c = triplet[0], triplet[1], triplet[2]

    return a**2 + b**2 == c**2