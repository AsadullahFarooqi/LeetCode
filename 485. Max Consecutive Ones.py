def findMaxConsecutiveOnes(nums):
    counter = 0
    answer = 0
    for num in nums:
        if num == 1:
            counter += 1
        else:
            answer = max(answer, counter)
            counter = 0
    answer = max(answer, counter)
    return answer


if __name__ == '__main__':
    A = [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1]
    A = [1,1,1,0,0,0,1,1,1,1,0]
    A = [1,0,1,1,0,1]
    print(findMaxConsecutiveOnes(A))