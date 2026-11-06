"""
N-Queens
"""

def count(n):
    return count_helper(n, 0, list(range(n)), [])

def count_helper(n, row, cols_remaining, locs):
    if row == n:
        return 1
    count = 0
    for i in range(len(cols_remaining)):
        if check(row, cols_remaining[i], locs):
            count += count_helper(n, row+1, cols_remaining[:i] 
            + cols_remaining[i+1:], locs + [[row, cols_remaining[i]]])

    return count

def check(row, col, locs):
    if len(locs) == 0:
        return True
    
    return (abs(row - locs[0][0]) != abs(col - locs[0][1]))and check(row, col, locs[1:])


if __name__ == "__main__":
    print(count(15))
