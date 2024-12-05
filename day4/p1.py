def safe_char(x, y, c):
    if x >= 0 and x < len(data) and y >= 0 and y < len(data[x]):
        return data[x][y] == c

    return False

# Load input into 2d array
with open('day4/input.txt') as f:
    data = f.readlines()
    data = [x.strip() for x in data]

count = 0

for x in range(len(data)):
    for y in range(len(data[x])):
        # Look for starting character
        if data[x][y] != 'A':
            continue

        if ( (safe_char(x - 1, y - 1, 'M') and safe_char(x + 1, y + 1, 'S')) or (safe_char(x - 1, y - 1, 'S') and safe_char(x + 1, y + 1, 'M'))) and ( (safe_char(x + 1, y - 1, 'M') and safe_char(x - 1, y + 1, 'S')) or (safe_char(x + 1, y - 1, 'S') and safe_char(x - 1, y + 1, 'M')) ):
            count += 1



print(count)
