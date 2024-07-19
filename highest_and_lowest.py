def high_and_low(string):
  high = 0
  low = 0

  arr = str.split(string, ' ')

  for char in arr:
      num = int(char)
      if num > high:
          high = num
      if num < low:
          low = num

  return f'{high} {low}'

print(high_and_low("8 3 -5 42 -1 0 0 -9 4 7 4 -4"))
