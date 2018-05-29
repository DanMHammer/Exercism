import re

def score(word):
    total = 0
    word = word.upper()

    total += len(re.findall(r"[AEIOULNRST]", word))
    total += len(re.findall(r"[DG]", word)) * 2
    total += len(re.findall(r"[BCMP]", word)) * 3
    total += len(re.findall(r"[FHVWY]", word)) * 4
    total += len(re.findall(r"[K]", word)) * 5
    total += len(re.findall(r"[JX]", word)) * 8
    total += len(re.findall(r"[QZ]", word)) * 10

    return total