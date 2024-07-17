def sort_gift_code(string):
  #bubble sort
    arr = list(string)
    last_i = len(arr) - 1
    while True:
        swaps = 0
        l = 0
        r = 1
        while r <= last_i:
            if arr[r] <= arr[l]:
                arr[l], arr[r] = arr[r], arr[l]
                swaps += 1
            l += 1
            r += 1
        if swaps == 0:
            return ''.join(arr)


print(sort_gift_code('ywusqomkigecabdfhjlnprtvxz'))
