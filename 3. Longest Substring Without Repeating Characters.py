from collections import Counter


class Solution:
    # def lswrc(s):
    #     if len(s) == 0:
    #         return 0
    #     elif len(s) == 1:
    #         return 1
    #     ans = float("-inf")
    #     for start in range(len(s)):
    #         d = {}
    #         end = start
    #         while end < len(s) and s[end] not in d:
    #             d[s[end]] = 1
    #             end += 1
    #         ans = max(ans, (end-start))
    #         # print(s[start:end])
    #     return ans
    
    
    def lengthOfLongestSubstring(self, s):
        start = 0
        longest = 0
        dicts = {}
        for index, char in enumerate(s):
            if char in dicts and start <= dicts[char]:
                start = dicts[char] + 1
            else:
                longest = max(longest, index - start + 1)
            dicts[char] = index
        return longest


if __name__ == '__main__':
    s = "pwwkew"
    sol = Solution()
    print(sol.lengthOfLongestSubstring(s))