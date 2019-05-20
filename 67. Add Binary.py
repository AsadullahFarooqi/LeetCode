def solution(a,b):
    a = "0"*abs(len(a)-len(b)) + a
    b = "0"*abs(len(a)-len(b)) + b
    ans = ""
    for i in range(len(a)-1, -1, -1):
        carry = 


if __name__ == '__main__':
    print(solution(a,b))
