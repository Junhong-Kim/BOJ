N = int(input())

numbers = []
for _ in range(N):
  numbers.append(int(input()))

for number in sorted(numbers):
  print(number)
