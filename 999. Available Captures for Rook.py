# git testing
def numRookCaptures(board):
    ans = 0
    rock_r, rock_c = finding_rock(board)
    # check up
    temp_r = rock_r-1
    c = board[temp_r][rock_c]
    while temp_r >= 0 and c == ".":
        c = board[temp_r][rock_c]
        temp_r -= 1
    if c != "." and c.lower() == c:
        ans += 1

    # check down
    temp_r = rock_r+1
    c = board[temp_r][rock_c]
    while temp_r < 8 and c == ".":
        c = board[temp_r][rock_c]
        temp_r += 1
    if c != "." and c.lower() == c:
        ans += 1

    # check left
    temp_c = rock_c-1
    c = board[rock_r][temp_c]
    while temp_c > -1 and c == ".":
        c = board[rock_r][temp_c]
        temp_c -= 1

    if c != "." and c.lower() == c:
        ans += 1

    # check right
    temp_c = rock_c+1
    c = board[rock_r][temp_c]
    while temp_c < 8 and c == ".":
        c = board[rock_r][temp_c]
        temp_c += 1

    if c != "." and c.lower() == c:
        ans += 1

    return ans

def finding_rock(board):
    R = 0
    C = 0
    for r in range(8):
        for c in range(8):
            if board[r][c] == "R":
                R = r
                C = c
                return r,c



if __name__ == '__main__':
    board = [
    [".",".",".",".",".",".",".","."],
    [".","p","p","p","p","p",".","."],
    [".","p","p","B","p","p",".","."],
    [".","p","B","R","B","p",".","."],
    [".","p","p","B","p","p",".","."],
    [".","p","p","p","p","p",".","."],
    [".",".",".",".",".",".",".","."],
    [".",".",".",".",".",".",".","."]]
    board = [
    [".",".",".",".",".",".",".","."],
    [".",".",".","p",".",".",".","."],
    [".",".",".","R",".",".",".","p"],
    [".",".",".",".",".",".",".","."],
    [".",".",".",".",".",".",".","."],
    [".",".",".","p",".",".",".","."],
    [".",".",".",".",".",".",".","."],
    [".",".",".",".",".",".",".","."]]
    print(numRookCaptures(board))
