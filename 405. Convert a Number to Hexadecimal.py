def tohex(num):
        if num < 0: return "ffffffff"
        elif num == 0: return 0

        d = {0: '0', 1: '1', 2: '2', 3: '3', 4: '4', 5: '5', 6: '6', 7: '7', 8: '8', 9: '9', 10: 'a', 11: 'b', 12: 'c', 13: 'd', 14: 'e', 15: 'f'}
        ans = ""
        while num > 0:
            x = num % 16
            num = num // 16
            ans += str(d[x])

        return ans[::-1]


if __name__ == '__main__':
    n = -1
    print(tohex(n))