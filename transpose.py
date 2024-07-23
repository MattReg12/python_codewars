def transpose(matrix):
    rows = len(matrix[0])

    new_arr = [[] for _ in range(rows)]

    for i, arr in enumerate(matrix):
        for i2, num in enumerate(arr):
            new_arr[i2].append(num)


    return new_arr
