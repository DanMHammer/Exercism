def is_armstrong(number):
    number_list = list(str(number))
    power = len(number_list)
    calculate = sum([int(x)**power for x in number_list])
    return number == calculate
