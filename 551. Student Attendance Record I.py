def checkrecord(s):
        a, l, p = 0, 0, 0

        for i in s:
            if i == "P":
                p += 1
            elif i == "A":
                a += 1
            else:
                l += 1

        return a < 2 or l < 3

if __name__ == '__main__':
    s = "LALL"
    print(checkrecord(s))
