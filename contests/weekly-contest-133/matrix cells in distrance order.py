def solution(R, C, r,c):
    ans = []
    for row in range(R):
        for col in range(C):
            d = abs(r-row)+abs(c-col)
            ans.append([d, row, col])
    ans = sorted(ans, key=lambda item: item[0])
    return [[x[1], x[2]] for x in ans]
    
if __name__ == '__main__':
    print(solution(2,2,0,1))