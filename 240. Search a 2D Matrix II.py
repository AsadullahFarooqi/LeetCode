class Solution:

    def searchMatrix(self, matrix, target):
        # bad way but still 36 ms o_O
        return any(target in row for row in matrix)


    def StefanPochmann_solution(self, matrix, target):
        j = -1
        for row in matrix:
            while j + len(row) and row[j] > target:
                j -= 1
            if row[j] == target:
                return True
        return False


if __name__ == '__main__':
    m = [[1,  4, 7,  11, 15],
        [2,   5,  8, 12, 19],
        [3,   6,  9, 16, 22],
        [10, 13, 14, 17, 24],
        [18, 21, 23, 26, 30]]
    t = 5
    m = [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]]
    t =5

    m = [
        [5, 8, 11,11,12,12,14,14,19],
        [9, 9, 14,17,17,19,21,26,27],
        [12,15,15,21,21,26,30,35,36],
        [17,17,20,25,28,30,32,35,39],
        [20,21,22,29,30,32,34,36,43],
        [24,24,25,31,36,40,40,43,45],
        [28,31,32,36,36,45,49,53,56],
        [29,33,36,39,40,50,54,57,57],
        [34,36,37,41,42,53,55,58,59],
        [37,40,42,44,47,53,56,58,62]]
    t = 22

    sol = Solution().optimized_pochmann_idea(m, t)
    print(sol)