def isSelfCrossing(x):
  n = sum(x[0::4])
  w = sum(x[1::4])
  s = sum(x[2::4])
  e = sum(x[3::4])
  
  return n >= s and e >= w

if __name__ == '__main__':
  l = [1,1,2,1,1]
  print(isSelfCrossing(l))