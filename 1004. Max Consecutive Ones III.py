class Solution:
    def longestOnes(self, A, K):
        left = right = 0
        ans = 0
        for left in range(len(A)):
            while right < len(A):
                if K <= 0 and A[right] == 0:
                    break
                if A[right] == 0:
                    K -= 1
                right += 1

            ans = max(ans, right-left)
            if A[left] == 0:
                K += 1        
        return ans
    def other_solution(self, a, k):
        #li-_-il solution
        st, res = 0, 0
        for i in range(len(a)):
            if a[i] == 0 and k:
                k -= 1
            elif a[i] == 0:
                while a[st] != 0:
                    st += 1
                st += 1              
            res = max(res, i-st+1)
        return res


    def lee215(self, A, K):
        i = 0
        for j in range(len(A)):
            K -= 1 - A[j]
            print(A[:j+1], A[j], 1- A[j])
            if K < 0:
                print(K, "i'm here")
                K += 1 - A[i]
                i += 1
        return j - i + 1

    def copy_lee(self, a,k):
        start = 0
        for end in range(len(a)):
            k -= 1-a[end]
            if k < 0:
                k += 1 - a[start]
                start += 1
        return end-start + 1


if __name__ == '__main__':
    A = [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1]
    K = 3
    A = [1,1,1,0,0,0,1,1,1,1,0]
    K = 2
    solution = Solution()
    print(solution.lee215(A, K))