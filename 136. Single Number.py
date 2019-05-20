def solution(nums):
    hash_ = {}
    for i in nums:
        if i in hash_:
            hash_[i] += 1
        hash_[i] = 1
    
    for k, v in hash_.items():
        if v == 1:
            return k


print(solution([2,2,1]))