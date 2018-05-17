def is_isogram(string):
    #remove hyphens and spaces and change all to lower
    string_no_hypens_spaces = string.replace(" ", "").replace("-", "").lower()
    #convert string_no_hypens_spaces to a list
    string_list = list(string_no_hypens_spaces)
    #also convert it to a set to remove duplicate characters
    string_set = set(string_no_hypens_spaces)
    #return comparison of their lengths. If it's an isogram, the list and set
    #are the same length, so it returns True.
    return len(string_set) == len(string_list)
