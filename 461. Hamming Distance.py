def solution(x, y):
    x, y = bin(x)[2:], bin(y)[2:]
    x = '0'*(abs(len(y)-len(x))) + x
    y = '0'*(abs(len(y)-len(x))) + y
    err = 0
    for i in range(len(y)):
        if x[i] != y[i]: err += 1
    return err

if __name__ == '__main__':
    solution(22, 1)