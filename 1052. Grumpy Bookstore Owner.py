class Solution(object):
    def maxSatisfied(self, customers, grumpy, X):
        # find the window 
        max_ = float("-inf")
        s = 0
        for i in range(len(customers)-X+1):
            t = self.unsatisfied(customers[i:i+X], grumpy[i:i+X])
            if t > max_:
                max_ = t
                s = i
        satesfied = 0
        for j in range(len(customers)):
            if grumpy[j] == 0:
                satesfied += customers[j]
            if grumpy[j] == 1 and j >= s and j < s+X:
                satesfied += customers[j]
        return satesfied                

    def unsatisfied(self, c, g):
        unsat = 0
        for i in range(len(c)):
            if g[i] == 1:
                unsat += c[i]
        return unsat

if __name__ == '__main__':
    c = [1,0,1,2,1,1,7,5]
    g = [0,1,0,1,0,1,0,1]
    x = 3

    sol = Solution().maxSatisfied(c, g, x)
    print(sol)

# [1,0,1,2,1,1,7,5]
# [0,1,0,1,0,1,0,1]