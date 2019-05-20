def longestPalindrome(s):
        if len(s) == 0:
            return s
        elif len(s) == 1 or s == s[::-1]:
            return s
        # ans = float("-inf")
        ans = ""
        for start in range(len(s)):
            for end in range(len(s), start, -1):
                temp = s[start:end]
                if  temp == temp[::-1] and len(temp) > len(ans):
                    ans = temp
        return ans

def is_palindrom(s):
    a = [0] * 26
    for i in s:
        a[ord(i)-ord("a")] += 1
    ignore = 0
    for i in a:
        if i % 2:
            ignore += 1
    return ignore < 2

if __name__ == '__main__':
    s = "cbbd"
    # print(is_palindrom(s))
    print(longestPalindrome(s))