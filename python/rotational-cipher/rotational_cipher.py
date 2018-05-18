import re


def rotate(text, key):

    # A-Z = 65 - 90 a-z = 97 - 122
    encoded = ""

    for char in text:
        if re.match(r"[A-Z]", char):
            if ord(char) + key > 90:
                encoded += chr((ord(char)+key) % 90 + 64)
            else:
                encoded += chr(ord(char)+key)
        elif re.match(r"[a-z]", char):
            if ord(char) + key > 122:
                encoded += chr((ord(char)+key) % 122 + 96)
            else:
                encoded += chr(ord(char)+key)
        else:
            encoded += char

    return encoded
