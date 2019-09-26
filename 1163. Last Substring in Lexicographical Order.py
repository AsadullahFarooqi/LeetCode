def lastSubstring(s):
    # Runtime: 724 ms, faster than 45.97% 
    # n = len(s)
    # poses = []
    # maxi = max(s)
    # pre = -2
    # print(poses, maxi, pre)
    # for i in range(n):
    #     if s[i] == maxi:
    #         if pre + 1 != i:
    #             poses.append(i)
    #             print(pre, i)
    #         pre = i
    # # print(poses)

    # res = ''
    # for pos in poses:
    #     res = max(res, s[pos:])
    # return res

    # i, j, k = 0, 1, 0
    # n = len(s)
    # while j + k < n:
    #     # print("i,j,k : ", i,j,k, "\ti+k : ", i+k, "\tj+k : ", j+k, end="\n  ")
    #     # print("s[i+k] : ", s[i+k], "\ts[j+k] : ", s[j+k])
    #     if s[i+k] == s[j+k]:
    #         k += 1
    #         continue
    #     elif s[i+k] > s[j+k]:
    #         # print("s[i+k] > s[j+k]")
    #         j = j + k + 1
    #     else:
    #         print("s[i+k] == s[j+k] \t", s[i+k], s[j+k], i+k+1,  i,k,j)
    #         i = max(i + k + 1, j)
    #         j = i + 1
    #     k = 0
    # return s[i:]

if __name__ == "__main__":
    # s = "xbylisvborylklftlkcioajuxwdhahdgezvyjbgaznzayfwsaumeccpfwamfzmkinezzwobllyxktqeibfoupcpptncggrdqbkji"
    # s = "dasad"
    s = "nnnp"
    # s = "zzzrziy"

    print(lastSubstring(s))