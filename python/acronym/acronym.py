import re

def abbreviate(words):
    words_list = re.split('\s|; |, |\*|\n|-', words)
    acronym = ""

    for word in words_list:
        acronym += word[0].upper()

    return acronym
