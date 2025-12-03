def solve():
    with open('input', 'r') as f:
        lines = f.readlines()

    total_joltage = 0
    for line in lines:
        line = line.strip()
        if not line:
            continue

        max_joltage = 0
        for i in range(len(line) - 1):
            d1 = int(line[i])
            max_d2 = 0
            for j in range(i + 1, len(line)):
                d2 = int(line[j])
                if d2 > max_d2:
                    max_d2 = d2
            
            joltage = d1 * 10 + max_d2
            if joltage > max_joltage:
                max_joltage = joltage

        total_joltage += max_joltage

    print(total_joltage)

solve()
