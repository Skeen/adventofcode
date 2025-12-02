def is_invalid(n):
    s = str(n)
    length = len(s)
    if length % 2 != 0:
        return False
    half = length // 2
    return s[:half] == s[half:]

def solve():
    with open("input", "r") as f:
        line = f.read().strip()
    
    total = 0
    ranges = line.split(',')
    for r in ranges:
        start, end = map(int, r.split('-'))
        for i in range(start, end + 1):
            if is_invalid(i):
                total += i
    
    print(total)

if __name__ == "__main__":
    solve()
