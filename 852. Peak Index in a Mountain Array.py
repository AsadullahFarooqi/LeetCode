def solution(A):
    if len(A) == 3:
        return 1
    for i in range(1, len(A)-1):
        if A[i-1] < A[i] and A[i] > A[i+1]:
            return i

print(solution([0, 2, 1, 0]))