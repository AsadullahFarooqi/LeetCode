def v(S, s, e):
        while s < e and S[s] == S[e]:
            s += 1
            e -= 1
        if S[s] != S[e]:
            return False
        return True

def validPalindrome(s):
        st = 0
        ed = len(s)-1
        err = 0
        while st <= ed and s[st] == s[ed]:
            st += 1
            ed -= 1
        
        if s[st] == s[ed]:
            return True
        elif s[st] != s[ed]:
            err += 1

        # remove from end then check
        if v(s, st, ed-1):
            return True
        # remove from start then check
        elif v(s, st+1, ed):
            return True

        return False


if __name__ == '__main__':
    tests = {
        "aba": True,
        "abca": True,
        "abead": False,
        "aewqqewea": False
    }

    for inp, out in tests.items():
        print(inp, "\n", "Solution Output: ", v(inp), "\n", "Expected Output: ", out)