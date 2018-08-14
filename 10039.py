scores = []

for _ in range(5):
    scores.append(int(input()))

for index, score in enumerate(scores):
    if score < 40:
        scores[index] = 40

total = sum(scores)
avg = total // 5
print(avg)
