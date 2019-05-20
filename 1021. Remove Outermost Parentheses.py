def solution1(S):
    ans = ""
    indecies = []
    stack = 0
    for i in range(len(S)):
        if stack == 0:
            indecies.append(i)
        if S[i] == "(": stack += 1
        else: stack -= 1
    if stack == 0: indecies.append(i+1)
    for i in range(len(indecies)-1):
        ans += S[indecies[i]+1:indecies[i+1]-1]
    return ans

if __name__ == '__main__':
    s = "(()())(())"
    # s = "(()())(())(()(()))"
    print(solution1(s))

# (()()) (()) (()(()))