def medianSlidingWindow(nums, k):
    ans = []
    o  = k % 2
    for i in range(len(nums)-k+1):
        temp = sorted(nums[i:i+k])
        if o:
            m = k // 2
            ans.append(temp[m])
            continue
        m = k//2
        ans.append((temp[m-1]+temp[m]) / 2)
        
    print(ans)

if __name__ == "__main__":
    n = [1,3,-1,-3,5,3,6,7]
    # print(len(n))
    medianSlidingWindow(n, 3)