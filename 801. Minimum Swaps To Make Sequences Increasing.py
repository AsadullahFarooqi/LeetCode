def swap(x,y):
    return y, x
def minswap(A, B):
    # swap = lambda a,b: y,x
    #wrong_location
    wl = 
    ans = 0
    for i in range(1, len(A)):
            if not A[i] > A[i-1]:
                # A[i], B[i] = swap(A[i], B[i])
                ans += 1
                continue

            if not B[i] > B[i-1]:
                # A[i], B[i] = swap(A[i], B[i])
                ans += 1
        #or not B[i] < B[i+1]
        # elif A[i] == A[i+1] and B[i] > B[i+1]:
        #     B[i], A[i] = swap(B[i], A[i])
        #     ans += 1
        # elif A[i] == A[i+1]:
        #     A[i], B[i] = swap(A[i], B[i])
        #     ans += 1

        # if :
        #     B[i], A[i] = swap(B[i], A[i])
        #     ans += 1
    return ans

if __name__ == '__main__':
    a = [3,3,8,9,10] #[0,4,4,5,9] # [1,3,5,4] # [0,3,5,8,9] #   
    b =  [1,7,4,6,8] #[0,1,6,8,10] # [1,2,3,7] #[2,1,4,6,9] #   
    print(minswap(a,b))
