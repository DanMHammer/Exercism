def flatten(iterable, limit=1000, counter=0):
    for i in range(len(iterable)):
        if (isinstance(iterable[i], (list, tuple)) and
            counter < limit):
            for a in iterable.pop(i):
                iterable.insert(i, a)
                i += 1
            counter += 1
            return flatten(iterable, limit, counter)
    output = []
    for elem in iterable:
        if elem is not None:
            output.append(elem)

    return output
