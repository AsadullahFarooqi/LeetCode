from collections import defaultdict

def lastSubstring(s):
    """ # crazy guy solution
        char = []
        for i in range(122, 96, -1):
            char.append(chr(i))
        for c in char:
            if c in s:
                print(c)
                for i, j in enumerate(s):
                    if s[i] == c:
                        # print(s[i:len(s)])
                        return(s[i:len(s)])
        max_c = s[0]
        for c in s:
            if c > max_c:
                # print(c,max_c)
                max_c = c

        max_sub = s[0]
        for i in range(len(s)):
            if s[i] == max_c:
                print(i, max_sub, s[i:])
                max_sub = max(max_sub, s[i:])

        return max_sub
    """

    n = len(s)

    poses = []
    maxi = max(s)
    pre = -2
    for i in range(n):
        if s[i] == maxi:
            if pre + 1 != i:
                poses.append(i)
            pre = i
    print(poses)

    res = ''
    for pos in poses:
        res = max(res, s[pos:])
    return res

if __name__ == "__main__":
    s = "xbylisvborylklftlkcioajuxwdhahdgezvyjbgaznzayfwsaumeccpfwamfzmkinezzwobllyxktqeibfoupcpptncggrdqbkji"
    # s = "dasad"
    print(lastSubstring(s[::-1]))