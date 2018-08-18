N = int(input())

numbers = list(map(int, input().split()))[:N]
count = 0

for number in numbers:
    for i in range(number, 0, -1):
        if i == number or number % i != 0:
            continue
        elif i == 1:
            count += 1
        elif number % i == 0:
            break
print(count)
