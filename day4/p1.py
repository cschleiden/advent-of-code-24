valid_directions = [
    [1, 0], # Right
    [-1, 0], # Left
    [0, 1], # Down
    [0, -1], # Up
    [1, 1], # Down Right
    [1, -1], # Up Right
    [-1, 1], # Down Left
    [-1, -1] # Up Left
]

def safe_char(x, y):
    if x >= 0 and x < len(data) and y >= 0 and y < len(data[x]):
        return data[x][y]

    return False

def match_word(sx, sy, dx, dy):
    sx += dx
    sy += dy
    if safe_char(sx, sy) != 'A':
        return False

    sx += dx
    sy += dy
    if safe_char(sx, sy) != 'S':
        return False

    return True

# Load input into 2d array
with open('day4/input.txt') as f:
    data = f.readlines()
    data = [x.strip() for x in data]

count = 0

for x in range(len(data)):
    for y in range(len(data[x])):
        # Look for starting character
        if data[x][y] != 'X':
            continue

        for direction in valid_directions:
            dx = direction[0]
            dy = direction[1]

            c = safe_char(x + dx, y + dy)
            if not c:
                continue

            if c != 'M':
                continue

            if match_word(x + dx, y + dy, dx, dy):
                count += 1

print(count)
