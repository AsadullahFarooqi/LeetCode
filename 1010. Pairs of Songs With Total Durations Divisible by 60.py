def numPairsDivisibleBy60(time):
        ans = []
        d = {}
        for x in time:
            d[abs(59-x)] = x

        for y in time:
            if y in d:
                print('i')
                ans .append([d[y], y])    
        return len(ans)

if __name__ == '__main__':
    n = [30,20,150,100,40]
    print(numPairsDivisibleBy60(n))