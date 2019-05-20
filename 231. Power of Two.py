from math import log
def ispoweroftwo(n):
        if n <= 0:
            return False
        x = 2
        while x <= n:
            x *= 2
            if x == n:
                return True
        return x != n
    # x = log(n, 2)
    # return int(x) == x
    
if __name__ == '__main__':
    # n = 536870912
    n = 1
    print(ispoweroftwo(n))