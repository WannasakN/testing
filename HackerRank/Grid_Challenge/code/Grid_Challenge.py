def gridChallenge(grid):
    if 1 <= len(grid) <= 100 :
        sorted_rows = map(sorted, grid)
        columns = zip(*sorted_rows)
        is_ordered = all(col == tuple(sorted(col)) for col in columns)
        return "YES" if is_ordered else "NO"

print(gridChallenge([]))
