import re
import secrets

#a = 97, z = 122

class Cipher(object):
    def __init__(self, key=None):
        if key:
            if len(re.findall(r"[a-z]", key)) != len(key):
                raise ValueError("Keys must contain lowercase letters only!")
            else:
                self.key = key
        else:
            self.key = "".join(list(map(lambda x: chr(int(x) + 97), str(secrets.randbits(1024)))))

    def encode(self, text):
        text = text.lower()
        chars = re.findall(r"[a-z]", text)
        output = ""
        key = [ord(x)-97 for x in self.key]

        if len(key) < len(text):
            key = key * (len(text)//len(key) + 1)

        for x in range(0, len(chars)):
            if ord(chars[x]) + key[x] > 122:
                #Add key[x], subtract 122, add 96 = + key[x] - 26
                output += chr(ord(chars[x]) + key[x] - 26)
            else:
                output += chr(ord(chars[x]) + key[x])

        return output

    def decode(self, text):
        output = ""
        key = [ord(x)-97 for x in self.key]

        if len(key) < len(text):
            key = key * (len(text) // len(key) + 1)

        for x in range(0, len(text)):
            if ord(text[x]) - key[x] < 97:
                # Find how far below 97 and then subtract that from 122. Left unsimplified for clarity.
                output += chr(122 - (96 - (ord(text[x]) - key[x])))
            else:
                output += chr(ord(text[x]) - key[x])

        return output


class Caesar(object):
    def __init__(self):
        pass

    def encode(self, text):
        text = text.lower()
        chars = re.findall(r"[a-z]", text)
        output = ""

        for char in chars:
            if ord(char) + 3 > 122:
                #Add 3, subtract 122, add 96 = -23.
                output += chr(ord(char) - 23)
            else:
                output += chr(ord(char) + 3)

        return output

    def decode(self, text):
        output = ""

        for char in text:
            if ord(char) - 3 < 97:
                #Add 97, subtract 3 = 94
                output += chr(ord(char) + 94)
            else:
                output += chr(ord(char) - 3)

        return output