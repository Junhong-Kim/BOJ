A = int(input())
B = int(input())
C = int(input())

result = A * B * C

for i in range(0, 10):
    count = str(result).count(str(i))
    print(count)
