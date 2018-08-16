word = input().upper()
total = 0

for char in word:
    if char in ['A', 'B', 'C']:
        total += 3
    elif char in ['D', 'E', 'F']:
        total += 4
    elif char in ['G', 'H', 'I']:
        total += 5
    elif char in ['J', 'K', 'L']:
        total += 6
    elif char in ['M', 'N', 'O']:
        total += 7
    elif char in ['P', 'Q', 'R', 'S']:
        total += 8
    elif char in ['T', 'U', 'V']:
        total += 9
    elif char in ['W', 'X', 'Y', 'Z']:
        total += 10
print(total)
