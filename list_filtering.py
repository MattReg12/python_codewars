def filter_list(arr):
    new_arr = []
    for elem in arr:
        if type(elem).__name__ != 'str':
            new_arr.append(elem)
    return new_arr
