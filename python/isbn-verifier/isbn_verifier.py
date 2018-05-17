import re

def verify(isbn):
    isbn_digits_and_X = re.findall(r"[0-9]+[X]+",isbn)
    if len(isbn_digits_and_X) != 10 or "X" in isbn_digits_and_X[:9]:
        return False

    isbn_x = isbn_digits_and_X.replace("X", 10)
    isbn_int = [int(x) for x in isbn_x]

    multiplier = 10
    total = 0

    for x in isbn_int:
        total += x * multiplier
        multiplier -= 1

    return total%11 == 0
