def solution(matrix):
    if len(matrix) == 0: return []
    elif len(matrix) < 2: return matrix[0]
    
    start_col, end_col = 0, len(matrix[0])-1
    start_row, end_row = 0, len(matrix)-1
    ans = []
    while start_row < end_row and start_col < end_col:
        # from top left -> top right
        col = start_col
        while col <= end_col:
            ans.append(matrix[start_row][col])
            col += 1
        start_row += 1
        
        # from top right -> bottom right
        row = start_row
        while row <= end_row:
            ans.append(matrix[row][end_col])
            row += 1
        end_col -= 1
        
        # from bottom right -> bottom left
        col = end_col
        while col >= start_col:
            ans.append(matrix[end_row][col])
            col -= 1
        end_row -= 1
        
        # from bottom left -> top left
        row = end_row
        while row >= start_row:
            ans.append(matrix[row][start_col])
            row -= 1
        start_col += 1
    return ans

if __name__ == "__main__":
    m = [
        [ 1, 2, 3 ],
        [ 4, 5, 6 ],
        [ 7, 8, 9 ]
    ]
    m2 = [[3,5,6,7], [1,2,3,4]]
    m3 = [
          [1,2,3,4],
          [5,6,7,8],
          [9,10,11,12]]

    print(solution(m3))

    
