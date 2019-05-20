def solution(costs):
    lsa = sorted(costs, key=lambda item: item[0])
    ans = 0
    for i in range(len(costs)//2):
        ans += lsa[i][0]
        costs.remove(lsa[i])
    bans = 0
    for j in costs:
        bans += j[1]
    return ans+bans


if __name__ == '__main__':
    
    print(solution([[10,20],[30,200],[400,50],[30,20]]))