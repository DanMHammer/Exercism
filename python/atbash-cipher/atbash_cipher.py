# A-Z = 65 - 90 a-z = 97 - 122
lower_ords = [x for x in range(97, 123)]
lower_cipher = dict(zip(lower_ords, lower_ords[::-1]))
#upper_ords = [x for x in range(65, 91)]
#upper_cipher = dict(zip(upper_ords, upper_ords[::-1]))
#cipher = {**lower_cipher, **upper_cipher}

def encode(plain_text):
    encoded = ""
    plain_text = plain_text.lower()

    for char in plain_text:
        try:
            int(char)
            encoded += char
            pass
        except(ValueError):
            pass
        if ord(char) in lower_cipher:
            encoded += chr(lower_cipher.get(ord(char)))
        else:
            pass

    encoded = " ".join([encoded[x:x+5] for x in range(0, len(encoded), 5)])

    return encoded

def decode(ciphered_text):

    decoded = ""

    for char in ciphered_text:
        try:
            int(char)
            decoded += char
            pass
        except(ValueError):
            pass
        if ord(char) in lower_cipher:
            decoded += chr(lower_cipher.get(ord(char)))
        else:
            pass

    return decoded
