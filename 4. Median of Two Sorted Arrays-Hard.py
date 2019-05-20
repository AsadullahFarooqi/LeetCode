def solution(nums1, nums2):
    pm = 0
    pn = 0
    ans = []
    while pm < len(nums1) and pn < len(nums2):
        if nums1[pm] <= nums2[pn]:
            ans.append(nums1[pm])
            pm += 1
        else:
            ans.append(nums2[pn])
            pn += 1
    if pm < len(nums1):
        ans += nums1[pm:]
    else:
        ans += nums2[pn:]

    print(ans)
    ans_l = len(ans)
    c = ans_l // 2
    if len(ans) % 2:
        return ans[c]
    else:
        return (ans[c - 1] + ans[c]) / 2

if __name__ == '__main__':
    l = list(map(int, input("enter list: ")))
    l2 = list(map(int, input("enter list: ")))
    print(solution(l, l2))
    