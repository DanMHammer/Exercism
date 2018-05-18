def slices(series, length):
    if length > len(series) or length < 1:
        raise ValueError("There are no slices of length {length} in {series}!")

    output = []
    num_slices = len(series) - length + 1

    for x in range(num_slices):
        output.append(series[x:x+length])

    return output
