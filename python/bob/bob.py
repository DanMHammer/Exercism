import re

def hey(phrase):
    #Remove unneccessary characters
    phrase = "".join(re.findall(r"[\w\d\.\?\!]",phrase))
    #Saying nothing
    if len(phrase) == 0:
        return 'Fine. Be that way!'
    #Yelling. Filter out all numbers so they don't get read as yelling
    elif phrase.upper() == phrase and re.search(r"[A-z]",phrase):
        if phrase.endswith('?'):
            return "Calm down, I know what I'm doing!"
        else:
            return 'Whoa, chill out!'
    # Calm Question
    elif phrase.endswith('?'):
        return 'Sure.'
    else:
        return 'Whatever.'
