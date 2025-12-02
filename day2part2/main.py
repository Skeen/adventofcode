def is_invalid(n):
    s = str(n)
    l = len(s)
    for i in range(1, l // 2 + 1):
        if l % i == 0:
            substring = s[:i]
            if substring * (l // i) == s:
                return True
    return False

def solve():
    with open("input", "r") as f:
        data = f.read().strip()

    ranges = data.split(',')
    total_sum = 0

    for r in ranges:
        start, end = map(int, r.split('-'))
        for i in range(start, end + 1):
            if is_invalid(i):
                total_sum += i
    
    print(total_sum)

if __name__ == "__main__":
    solve()