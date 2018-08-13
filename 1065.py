def compute(n):
    nums = []
    while n > 0:
        nums.append(n % 10)
        n = n // 10
    return nums


count = 0
N = int(input())
for i in range(1, N + 1):
    try:
        numbers = compute(i)
        d = int(numbers[-1] - numbers[0]) / (len(numbers) - 1)
        for index, number in enumerate(numbers):
            try:
                if number + d != numbers[index + 1]:
                    break
            except IndexError:
                count += 1
    except ZeroDivisionError:
        count += 1
        pass

print(count)
