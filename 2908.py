A, B = input().split()

reversed_a = ''.join(reversed(A))
reversed_b = ''.join(reversed(B))

if int(reversed_a) > int(reversed_b):
    print(reversed_a)
else:
    print(reversed_b)
