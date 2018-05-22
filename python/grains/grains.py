def on_square(integer_number):
    validate(integer_number)
    return 2**(integer_number-1)


def total_after(integer_number):
    validate(integer_number)
    return 2**integer_number - 1


def validate(integer_number):
    if integer_number not in range(1,65):
        raise ValueError("The number must be from 1 to 64.")