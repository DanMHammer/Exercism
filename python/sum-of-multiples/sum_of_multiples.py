def sum_of_multiples(limit, multiples):

    multiple_set = set()
    
    for number in multiples:
        multiple_set = multiple_set.union([i for i in range(0, limit, number)])

    return sum(multiple_set)
