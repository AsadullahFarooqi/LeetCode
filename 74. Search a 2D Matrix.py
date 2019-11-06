class Solution:
    def searchMatrix(self, matrix, target):
        if not len(matrix) or not len(matrix[0]) or matrix[0][0] > target or matrix[-1][-1] < target:
            return False
        elif matrix[0][0] == target or matrix[-1][-1] == target:
            return True

        # finding row
        s, e = 0, len(matrix)-1
        r = None
        m = 0
        # print(matrix[m][0] <= target, matrix[m][-1]  >= target)
        if matrix[s][0] <= target and matrix[s][-1] >= target:
            r = s
        elif matrix[e][0] <= target and matrix[e][-1] >= target:
            r = e

        while s <= e and r == None:
            m = (s+e) // 2
            if matrix[m][0] <= target and matrix[m][-1] >= target:
                r = m
            elif matrix[m][0] > target:
                e = m-1
            else:
                s = m+1

        if r == None:
            return False
        # finding column
        s, e = 0, len(matrix[r])-1
        while s <= e:
            m = (s+e) // 2
            if matrix[r][m] == target or matrix[r][s] == target or matrix[r][e] == target:
                return True
            elif matrix[r][m] > target:
                e = m-1
            else:
                s = m+1

        return False


if __name__ == '__main__':
    m = [[1,   3,  5,  7],
        [10, 11, 16, 20],
        [23, 30, 34, 50]]
    t = 16

    # m = [[1],[3],[5]]
    # t = 3
    
    # m = [[1,3,5,7],[10,11,16,20],[23,30,34,50]]
    # t = 23
    
    # m = [[1], [3]]
    # t = 2
    
    # m = [[1,3,5,7],[10,11,16,20],[23,30,34,50]]
    # t = 30
    
    # m = [[1,3,5,7],[10,11,16,20],[23,30,34,50]]
    # t = 7
    m = [[-8,-7,-5,-3,-3,-1,1],[2,2,2,3,3,5,7],[8,9,11,11,13,15,17],[18,18,18,20,20,20,21],[23,24,26,26,26,27,27],[28,29,29,30,32,32,34]]
    t = -5
    sol = Solution().searchMatrix(m, t)
    print(sol)