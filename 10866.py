N = int(input())
d = []


def deck(cmd):
    if cmd[0] == 'push_front':
        d.insert(0, int(cmd[1]))
    elif cmd[0] == 'push_back':
        d.append(int(cmd[1]))
    elif cmd[0] == 'pop_front':
        try:
            print(d.pop(0))
        except IndexError:
            print(-1)
    elif cmd[0] == 'pop_back':
        try:
            print(d.pop())
        except IndexError:
            print(-1)
    elif cmd[0] == 'size':
        print(len(d))
    elif cmd[0] == 'empty':
        if len(d):
            print(0)
        else:
            print(1)
    elif cmd[0] == 'front':
        try:
            print(d[0])
        except IndexError:
            print(-1)
    elif cmd[0] == 'back':
        try:
            print(d[-1])
        except IndexError:
            print(-1)


if __name__ == '__main__':
    for _ in range(N):
        deck(input().split())
