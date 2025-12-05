
def solve():
    with open('input', 'r') as f:
        lines = f.readlines()

    fresh_ranges = []
    available_ids = []
    parsing_ranges = True

    for line in lines:
        line = line.strip()
        if not line:
            parsing_ranges = False
            continue

        if parsing_ranges:
            start, end = map(int, line.split('-'))
            fresh_ranges.append((start, end))
        else:
            available_ids.append(int(line))

    fresh_count = 0
    for ingredient_id in available_ids:
        is_fresh = False
        for start, end in fresh_ranges:
            if start <= ingredient_id <= end:
                is_fresh = True
                break
        if is_fresh:
            fresh_count += 1

    print(fresh_count)

if __name__ == "__main__":
    solve()
