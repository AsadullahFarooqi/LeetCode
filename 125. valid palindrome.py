def sol(s):
        a = ""
        A = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
        for i in s.lower():
            if i in A:
                a += i
        return a == a[::-1]


if __name__ == '__main__':
    tests = {
        "A man, a plan, a canal: Panama": True,
        "race a car": False,
        "0P": False,
        "ab2a":False,
    }

    for inp, out in tests.items():
        print(inp, "\n", "Solution Output: ", sol(inp), "\n", "Expected Output: ", out)