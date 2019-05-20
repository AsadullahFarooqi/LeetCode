def lswrc(s):
    if len(s) == 0:
        return 0
    elif len(s) == 1:
        return 1
    ans = float("-inf")
    for start in range(len(s)):
        d = {}
        end = start
        while end < len(s) and s[end] not in d:
            d[s[end]] = 1
            end += 1
        ans = max(ans, (end-start))
        # print(s[start:end])
    return ans

if __name__ == '__main__':
    s = "pwwkew"
    print(lswrc(s))