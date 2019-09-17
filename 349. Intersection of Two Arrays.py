def intersection(nums1, nums2):
    intersection_map = {k:False for k in nums1}
    
    for i in nums2:
        if i in intersection_map:
            intersection_map[i] = True

    return [k for k,v in intersection_map.items() if v == True]


if __name__=="__main__":
    #n,m=[1,2,2,1],[2,2]
    n,m=[4,9,5],[9,4,9,8,4]
    print(intersection(n,m))
