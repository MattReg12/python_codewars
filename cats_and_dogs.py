# Array of dogs, and a number
# Each dog can only catch one cat. But it can catch cats more than n indices away.
#

# copy the array
# iterate through the given array
# if C, skip,
# if D, check i - N as long as positive backwards,
    # if C, check to see if marked in copy array
      # if not, mark
      # if marked, continue
    # if D, continue process at +1 intervals until 2i is greater than N.


def solve(arr, n):
    caught_array = arr[:]
    for i, animal in enumerate(arr):
        constant_i = i
        if animal == 'C':
            continue
        else:
            i -= n
            while (i <= (constant_i + n) and i < len(arr)):
                if i < 0 or arr[i] == 'D':
                    i += 1
                    continue
                else:
                    already_caught = caught_array[i] == True
                    if already_caught:
                        i += 1
                        continue
                    else:
                        caught_array[i]  = True
                        break
    return caught_array.count(True)




print(solve(['D','C','C','D','C'], 1))
print(solve(['C','C','D','D','C','D'],2))
print(solve(['C','C','D','D','C','D'],1))
print(solve(['D','C','D','C','C','D'],3))
print(solve(['C','C','C','D','D'],3))
print(solve(['C','C','C','D','D'],2))
print(solve(['C','C','C','D','D'],1))
