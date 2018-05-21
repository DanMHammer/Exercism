"""Global variable. List of neccessary digit words."""
words = {0: "zero", 1: "one", 2: "two", 3: "three", 4: "four", 5: "five",
            6: "six", 7: "seven", 8: "eight", 9: "nine", 10: "ten",
            11: "eleven", 12: "twelve", 13: "thirteen", 14: "fourteen",
            15: "fifteen", 16: "sixteen", 17: "seventeen", 18: "eighteen",
            19: "nineteen", 20: "twenty", 30: "thirty", 40: "forty",
            50: "fifty", 60: "sixty", 70: "seventy", 80: "eighty",
            90: "ninety"}


def say(number):
    """Say the name of numbers."""
    output = []
    validate(number)
    if number == 0:
        return 'zero'
    places_list = separate(number)

    if places_list[0] != 0:
        output.append(value_to_word(places_list[0]))
        output.append("billion")
    if places_list[1] != 0:
        output.append(value_to_word(places_list[1]))
        output.append("million")
    if places_list[2] != 0:
        output.append(value_to_word(places_list[2]))
        output.append("thousand")
    if places_list[3] != 0:
        if (places_list[0] != 0 or places_list[1] != 0)\
                and places_list[2] == 0:
            output.append("and")
        output.append(value_to_word(places_list[3]))

    return " ".join(output)


def validate(number):
    """Validate the input. Reject numbers that are too large or negative."""
    if number < 0:
        raise ValueError("Inputs must be positive!")
    if number >= 1e12:
        raise ValueError("{number} is too large. Input number less than 1e12")
    if number == 0:
        return "zero"


def separate(place):
    """Separate initial number into 10^3 places."""
    places_list = [0, 0, 0, 0]
    if place//1000000000 >= 1:
        places_list[0] = place//1000000000
        place = place % 1000000000
    if place//1000000 >= 1:
        places_list[1] = place//1000000
        place = place % 1000000
    if place//1000 >= 1:
        places_list[2] = place//1000
        place = place % 1000
    if place % 1000 > 0:
        places_list[3] = place % 1000
    return places_list


def value_to_word(value):
    """Convert the place value to a word."""
    value_word = []
    value = value % 1000
    if value >= 100:
        value_word.append(words.get(value//100))
        value_word.append("hundred")
        value = value % 100
        if value != 0:
            value_word.append("and")
    if value > 19 and value % 10 != 0:
        value_word.append(words.get(value//10 * 10)
                          + "-" + words.get(value % 10))
    elif value != 0:
        value_word.append(words.get(value))

    return " ".join(value_word)
