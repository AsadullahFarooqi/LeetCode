def largestPerimeter(A):
  A.sort()
  A.reverse()
  max_size = 0
  for i in range(len(A)-2):
    for j in range(i+1, len(A)-1):
      for k in range(j+1, len(A)):
        a, b, c = A[i], A[j], A[k]
        if checker(a, b, c) and a+b+c > max_size:
          max_size = a+b+c
  return max_size

def checker(a, b, c):
  return a+b > c and a+c > + b and b+c > a

if __name__ == '__main__':
  l = list(map(int, input("enter list: ")))
  print(largestPerimeter(l))