def get_larger_numbers(a, b):
    arr = []
    for i in range(len(a)):
        arr.append(max(a[i], b[i]))
    return arr
