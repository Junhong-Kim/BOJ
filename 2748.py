n = int(input())

fib1 = 0
fib2 = 1
fib3 = None

for i in range(n):
    fib3 = fib1 + fib2
    fib2 = fib1
    fib1 = fib3
print(fib3)
