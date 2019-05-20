def validMountainArray(A):
        if len(A) < 3:
            return False
        i = 0
        while i < len(A)-1 and A[i] < A[i+1]:
            i += 1

        if i == 0 or i == len(A)-1:
            return False

        while i < len(A)-1 and A[i] > A[i+1]:
            i += 1

        if i < len(A)-1:
            return False

        return True


if __name__ == '__main__':
    n = [0,1,2,3,4,5,6,7,8,9]
    print(validMountainArray(n))