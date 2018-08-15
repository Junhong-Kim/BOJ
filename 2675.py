T = int(input())

for i in range(T):
    R, S = input().split()

    ret = ''
    chars = list(S)
    for char in chars:
        ret += (char * int(R))
    print(ret)
