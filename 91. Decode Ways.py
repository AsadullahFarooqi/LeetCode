class Solution:
    def numDecodings(self, s: str) -> int:
        # ans = 1
        # for i in range(len(s)-2):
        #     if int(s[i:i+2]) < 27:
        #         ans += 1
        # return ans

        # w tells the number of ways
        # v tells the previous number of ways
        # d is the current digit
        # p is the previous digit

        
        # v, w, p = 0, int(s>''), ''
        # for d in s:
        #     v, w, p = w, (d>'0')*w + (9<int(p+d)<27)*v, d
        # return w

        v = 0
        w = int(s>'')
        p = ''
        for d in s:
            v = w
            w = (d>'0')*w + (9<int(p+d)<27)*v
            print((d>'0')*w + (9<int(p+d)<27)*v)
            p = d
        return w

if __name__ == '__main__':
    s = "226"
    sol = Solution()
    print(sol.numDecodings(s))