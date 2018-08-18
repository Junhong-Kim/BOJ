N = int(input())
s = []


def queue(cmd):
    if cmd[0] == 'push':
        s.append(int(cmd[1]))
    elif cmd[0] == 'pop':
        try:
            print(s.pop(0))
        except IndexError:
            print(-1)
    elif cmd[0] == 'front':
        try:
            print(s[0])
        except IndexError:
            print(-1)
    elif cmd[0] == 'back':
        try:
            print(s[-1])
        except IndexError:
            print(-1)
    elif cmd[0] == 'size':
        print(len(s))
    elif cmd[0] == 'empty':
        if len(s):
            print(0)
        else:
            print(1)


if __name__ == '__main__':
    for _ in range(N):
        queue(input().split())
