def solution(nums):
	if len(nums) == 1:
		return 1
	elif len(nums) == 2:
		if sorted(nums) == nums:
			return len(nums)
		return 1
	s, e = 0, 0
	ans = []
	for i in range(1, len(nums)):
		if nums[i] < nums[e]:
			print(nums[s:i])
			ans.append(i-s)
			e = i
			s = i
			continue
		e += 1
	return max(ans)

if __name__ == '__main__':
	n = [10,9,2,5,3,7,101,18]
	print(solution(n))