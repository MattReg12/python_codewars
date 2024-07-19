import math

def count_bits(n):
    count = 0
    while (n > 0):
        n -= (2**(math.floor(math.log2(n))))
        count += 1

    return count

print(count_bits(1234))
