def merge_ranges(ranges):
    """Merges overlapping ranges."""
    if not ranges:
        return []

    # Sort ranges by their starting points
    ranges.sort(key=lambda x: x[0])

    merged_ranges = []
    current_start, current_end = ranges[0]

    for next_start, next_end in ranges[1:]:
        if next_start <= current_end:
            # Overlapping range, merge it
            current_end = max(current_end, next_end)
        else:
            # Disjoint range, start a new one
            merged_ranges.append((current_start, current_end))
            current_start, current_end = next_start, next_end

    merged_ranges.append((current_start, current_end))
    return merged_ranges

def main():
    """Reads ranges from input, merges them, and calculates the total count."""
    ranges = []
    with open("input", "r") as f:
        for line in f:
            line = line.strip()
            if not line or not '-' in line:
                # Stop reading after the ranges section
                break
            start, end = map(int, line.split('-'))
            ranges.append((start, end))

    merged = merge_ranges(ranges)

    total_fresh_ids = 0
    for start, end in merged:
        total_fresh_ids += end - start + 1

    print(f"Total fresh ingredient IDs: {total_fresh_ids}")

if __name__ == "__main__":
    main()