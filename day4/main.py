
def solve():
    with open('input', 'r') as f:
        grid = [line.strip() for line in f]

    rows = len(grid)
    cols = len(grid[0])
    accessible_rolls = 0

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == '@':
                adjacent_rolls = 0
                for dr in [-1, 0, 1]:
                    for dc in [-1, 0, 1]:
                        if dr == 0 and dc == 0:
                            continue

                        nr, nc = r + dr, c + dc

                        if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == '@':
                            adjacent_rolls += 1
                
                if adjacent_rolls < 4:
                    accessible_rolls += 1
    
    print(accessible_rolls)

solve()
