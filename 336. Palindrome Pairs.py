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

if __name__ == '__main__':
    s = "cbbd"
    # print(is_palindrom(s))
    print(longestPalindrome(s))