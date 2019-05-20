def solution(S, K):
    s = "".join(S.split("-")).upper()
    ans = ""
    start = 0

    end = len(s)%K
    step = len(s)//K
    
    while start < len(s):
        ans += s[start:end] + "-"
        start = end
        end += step
    print(ans)
if __name__ == '__main__':
    k = int(input("enter number K: "))
    l = input("enter list: ")
    solution(l, k)