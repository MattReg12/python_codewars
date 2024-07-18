# create dict, keys = string num, values = word nums
# convert arg to string
# convert string to arr and map to dict values
# join str and create arr with this as first

# until last index is four

# counter letters and convert to string
# if len of string > 1, break down --- helper function

NUMBER_WORDS = {
    '0': 'zero',
    '1': 'one',
    '2': 'two',
    '3': 'three',
    '4': 'four',
    '5': 'five',
    '6': 'six',
    '7': 'seven',
    '8': 'eight',
    '9': 'nine'
}

EQUILIBRIUM = 'four'

def last(arr):
    return arr[-1]

def convert_num_to_countstring(num):
    arr = list(str(num))
    arr = [NUMBER_WORDS[char] for char in arr]
    return ''.join(arr)

def numbers_of_letters(n):
    arr = [convert_num_to_countstring(n)]
    while (last(arr) != EQUILIBRIUM):
        arr.append(convert_num_to_countstring(len(last(arr))))
    return arr


print(numbers_of_letters(1), ["one", "three", "five", "four"])
print(numbers_of_letters(12), ["onetwo", "six", "three", "five", "four"])
print(numbers_of_letters(37), ["threeseven", "onezero", "seven", "five", "four"])
print(numbers_of_letters(311), ['threeoneone', 'oneone', 'six', 'three', 'five', 'four'])
print(numbers_of_letters(999), ["nineninenine", "onetwo", "six", "three", "five", "four"])
