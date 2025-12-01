
def solve():
    position = 50
    password = 0
    with open('input', 'r') as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            direction = line[0]
            distance = int(line[1:])
            if direction == 'L':
                position = (position - distance) % 100
            elif direction == 'R':
                position = (position + distance) % 100
            if position == 0:
                password += 1
    print(password)

if __name__ == '__main__':
    solve()
