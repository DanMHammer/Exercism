#Does not pass test_unique_return_values

SUBLIST = True
SUPERLIST = True
EQUAL = True
UNEQUAL = True

def check_lists(first_list, second_list):

    if first_list == second_list:
        return EQUAL

    if first_list in second_list:
        return SUBLIST

    if second_list in first_list:
        return SUPERLIST

    else:
        return UNEQUAL