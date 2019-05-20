def main(A):
    rep_hash = {}
    for i in A:
        if i in rep_hash:
            rep_hash[i] += 1
        else:
            rep_hash[i] = 1
    m  = max(rep_hash.values())
    for k,v in rep_hash.items():
        if v == m:
            return k
    print(rep_hash)

def sol(A):
    even = []
    odd = []
    for i in A:
        if i%2:
            odd.append(i)
        else:
            even.append(i)
    return even+odd

if __name__ == '__main__':
    ls = [1,2,3,4]
    print(sol(ls))
