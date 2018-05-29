import string
import math

def encode(plain_text):

    text = "".join(list(filter(lambda x: x in string.ascii_letters or x in string.digits, plain_text))).lower()

    if not text:
        return ''

    c = int(math.ceil(len(text)**.5))

    square = []

    for x in range(0, len(text), c):
        square.append(text[x:x+c])

    #Pad the end
    while len(square[-1]) != c:
        square[-1] += " "

    output = ""

    for x in range(0, c):
        for y in range(0, len(square)):
            output += square[y][x]
        output += " "

    #Remove superfluous space
    return output[:-1]