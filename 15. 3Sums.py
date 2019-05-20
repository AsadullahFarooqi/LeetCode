from itertools import combinations
def threeSum(nums):
    # ans = set()
    # for i in combinations(nums, 3):
    #     if sum(i) == 0:
    #         i = [str(x) for x in sorted(i)]
    #         ans.add(",".join(i))
    # ans = list(ans)
    # print(ans)
    # ls = []    
    # for i in ans:
    #     ls.append([int(x) for x in i.split(",")])
    # return ls

    

if __name__ == '__main__':
    nums = [-1, 0, 1, 2, -1, -4]
    print(threeSum(nums))