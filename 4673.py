def compute_num(num):
    total = num
    while num > 0:
        total += (num % 10)
        num = (num // 10)
    return total


numbers = []
for i in range(10000):
    numbers.append(compute_num(i))


for i in range(10000):
    if i not in numbers:
        print(i)
