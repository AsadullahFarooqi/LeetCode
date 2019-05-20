def mySqrt(x: int) -> int:
  i = 0
  while i <= x//2:
    if i**2 == x or (i+1)**2 > x and i**2 < x:
      return i
    i += 1

if __name__ == '__main__':
    i = 2
    while i > 1:
        i = int(input("enter number: "))
        print("Case #{}: {}".format(i, mySqrt(i)))
