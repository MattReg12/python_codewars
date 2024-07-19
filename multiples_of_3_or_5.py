def solution(n):
    if (n < 0):
        return 0

    nums = []
    pattern = [2, 1, 3, 1, 2, 3, 3]
    i = 0
    f = 3
    while (f < n):
        nums.append(f)
        f += pattern[i]
        i = 0 if i == 6 else i + 1

    return sum(nums)

print(solution(4), 3)
print(solution(6), 8)
print(solution(16), 60)
print(solution(3), 0)
print(solution(5), 3)
print(solution(15), 45)
print(solution(0), 0)
print(solution(-1), 0)
print(solution(10), 23)
print(solution(20), 7)
print(solution(200), 9168)

