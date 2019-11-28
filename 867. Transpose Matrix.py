class Solution(object):
    def transpose(self, A):
        if not A or not len(A[0]):
            return A
        ans = [[] for i in range(len(A[0]))]
        for row in A:
            for i in range(len(ans)):
                ans[i].append(row[i])
        return ans


if __name__ == '__main__':
    a = [[1,2,3],[4,5,6],[7,8,9]]
    a = [[1,2,3],[4,5,6]]

    sol = Solution().transpose(a)
    print(sol)