def solve():
    total_joltage = 0
    with open('input', 'r') as f:
        for line in f:
            line = line.strip()
            if not line:
                continue

            num_digits_to_keep = 12
            k = len(line) - num_digits_to_keep

            if k < 0:
                # This case should not happen based on input, but good to handle
                # If line is shorter than 12, just use the line as is.
                total_joltage += int(line)
                continue

            result_stack = []
            for digit in line:
                while k > 0 and result_stack and digit > result_stack[-1]:
                    result_stack.pop()
                    k -= 1
                result_stack.append(digit)
            
            # The result might be longer than `num_digits_to_keep` if we didn't use all `k` removals
            # (e.g., for a descending sorted string). The smallest digits will be at the end of the stack.
            # So we just need the first `num_digits_to_keep` digits from our optimized result.
            joltage_str = "".join(result_stack[:num_digits_to_keep])
            total_joltage += int(joltage_str)

    print(total_joltage)

if __name__ == "__main__":
    solve()
