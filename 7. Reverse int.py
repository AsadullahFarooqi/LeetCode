def solution(x):
    if x < (-2**31) or x > (2**31)-1:
        return 0
    x = str(x)
    if x[0] == "-":
        x = x[1:]
        x = -1 * int(x[::-1])
    else:
        x = int(x[::-1])
    
    if x >= (-2**31) and x <= (2**31)-1:
        return x
    return 0

if __name__ == '__main__':
    print(solution(2147483651))