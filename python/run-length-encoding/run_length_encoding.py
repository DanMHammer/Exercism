import re

def decode(string):
    if string == "":
        return ""
    string_str_int = []
    for x in range(0, len(string)):
        try:
            if re.match(r"[0-9]", string[x]) and re.match(r"[0-9]", string[x+1]):
                string_str_int.append(int(string[x]+string[x+1]))
                string = string[:x+1] + string[x+2:]
            elif re.match(r"[0-9]", string[x]):
                string_str_int.append(int(string[x]))
            else:
                string_str_int.append(string[x])
        except(IndexError):
          pass
    if isinstance(string_str_int[0],int):
        list_padded = []
    else:
        list_padded = [1]
    for x in range(0, len(string_str_int)):
        list_padded.append(string_str_int[x])
        try:
            if isinstance(string_str_int[x], str) and isinstance(string_str_int[x+1], str):
                list_padded.append(1)
        except(IndexError):
            pass

    ints = list_padded[::2]
    strings = list_padded[1::2]

    decoded = "".join([ints[x]*strings[x] for x in range(0, len(strings))])

    return decoded

def encode(string):
    if string == "":
        return ""
    group_chars = [string[0]]
    group_count = 0
    for x in range(1, len(string)):
        if string[x] in string[x-1]:
            group_chars[group_count] += string[x]
        else:
            group_count += 1
            group_chars.append(string[x])

    for x in range(0, len(group_chars)):
        if len(group_chars[x]) > 1:
            group_chars[x] = str(group_chars[x].count(group_chars[x][0])) + group_chars[x][0]
        else:
            group_chars[x] = group_chars[x][0]
    return "".join(group_chars)
