from math import gcd

def primitive_triplets(number_in_triplet):
    pass


def triplets_in_range(range_start, range_end):
    z = 0
    triplets = set()
    for c in range(range_start, range_end):
        for a in range(range_start, range_end):
            try:
                b = round((c**2 - a**2)**.5)
                if gcd(a, b) == 1:
                    triplets.add(tuple(a, b, c))
            except(TypeError):
                pass
    return triplets

def is_triplet(triplet):
    pass