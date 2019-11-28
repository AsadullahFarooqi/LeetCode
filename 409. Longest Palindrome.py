class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        hash_map = {}
        for i in s:
            if not i in hash_map:
                hash_map[i] = 0
                
            hash_map[i] += 1
        ans = 0
        leave_one_odd = True
        for k,v in hash_map.items():
            if leave_one_odd and v%2:
                ans += v
                leave_one_odd = False
            elif v%2:
                ans += v-1
            else:
                ans += v
        return ans

if __name__ == '__main__':
    inp = "abccccdd"
    sol = Solution().longestPalindrome(inp)
    print(sol)