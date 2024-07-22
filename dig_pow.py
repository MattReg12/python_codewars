def dig_pow(n, p):
    num_string = str(n)
    sum = 0
    for i in range(0, len(num_string)):
        sum += int(num_string[i])**(p + i)

    return int(sum / n) if (sum % n == 0) else -1

print(dig_pow(89, 1), 1)
print(dig_pow(92, 1), -1)
print(dig_pow(46288, 3), 51)
print(dig_pow(41, 5), 25)
print(dig_pow(114, 3), 9)
print(dig_pow(8, 3), 64)
