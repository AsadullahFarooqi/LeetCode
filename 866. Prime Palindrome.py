def primePalindrome(N):
    for i in prime_numbers(N):
        s = str(i)
        if s == s[::-1]:
            return i

def prime_numbers(n):
    i = n+1
    while True:
        j = 2
        while(j <= int(i**0.5)):
            if not(i%j): break
            j = j + 1
        if (j > i/j) :
            yield i
        i = i + 1

if __name__ == '__main__':
    # n = 9989900
    n = 8
    print(primePalindrome(n))