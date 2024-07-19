def filter_list(arr):
    new_arr = []
    for elem in arr:
        if type(elem).__name__ != 'str':
            new_arr.append(elem)
    return new_arr

print(filter_list([1,2,'a','b']))
print(filter_list([1,'a','b',0,15]))
print(filter_list([1,2,'aasf','1','123',123]))
