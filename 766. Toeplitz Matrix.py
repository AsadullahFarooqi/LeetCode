def isToeplitzMatrix(matrix):
    groups = {}
    for r, row in enumerate(matrix):
        print(r,row)
        for c, val in enumerate(row):
            print(c, val)
            if r-c not in groups:
                groups[r-c] = val
            elif groups[r-c] != val:
                return False
    print(groups)
    return True


if __name__ == '__main__':
    matrix = [
    [1,2,3,4],
    [5,1,2,3],
    [9,5,1,2]]
    print(isToeplitzMatrix(matrix))