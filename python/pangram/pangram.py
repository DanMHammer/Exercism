import re

def is_pangram(sentence):
    #Only extract alphabet characters. Convert to lower case
    sentence_alphabet = "".join(re.findall(r"[a-zA-Z]+", sentence)).lower()
    #Convert to a set to remove duplicates and return True if it is exactly 26 characters.
    return len(set(sentence_alphabet)) == 26
