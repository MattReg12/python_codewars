def check_three_and_two(array):
    hash = {}
    for string in array:
        count = hash.get(string) or 0
        hash[count] = count + 1

    vals = len(list(hash.values()))
    return vals == [3,2] or vals == [2, 3]
