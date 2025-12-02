def solve():
    with open('input', 'r') as f:
        rotations = f.readlines()

    dial_position = 50
    zero_count = 0

    for rotation in rotations:
        direction = rotation[0]
        distance = int(rotation[1:])

        if direction == 'L':
            for _ in range(distance):
                dial_position -= 1
                if dial_position < 0:
                    dial_position = 99
                if dial_position == 0:
                    zero_count += 1
        elif direction == 'R':
            for _ in range(distance):
                dial_position += 1
                if dial_position > 99:
                    dial_position = 0
                if dial_position == 0:
                    zero_count += 1
    
    # The problem is a bit ambiguous about whether the final landing on 0 counts
    # "during a rotation". The examples suggest it does. Let's stick with the current logic.
    # The initial position is 50, so we don't start at 0.

    print(f"The password is: {zero_count}")

solve()