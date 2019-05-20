def judgeSquareSum(c: int) -> bool:
  c2 = int((c+1)**0.5)+1
  for a in range(c2):
    b = c - a**2
    temp = b**0.5
    print(a, temp, c - a**2)
    if b >= 0 and int(temp) == temp:
      return True
  return False


if __name__ == '__main__':
  i = 2
  while i > 1:
    i = int(input("enter number: "))
    print("Case #{}: {}".format(i, judgeSquareSum(i)))