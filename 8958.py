N = int(input())

for _ in range(N):
    total = 0
    score = 0
    results = list(input())
    for index, result in enumerate(results):
        if result == 'X':
            score = 0
        else:
            score += 1
            total += score
    print(total)
