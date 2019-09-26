"""
We have a collection of rocks, each rock has a positive integer weight.

Each turn, we choose the two heaviest rocks and smash them together.  Suppose the stones have weights x and y with x <= y.  The result of this smash is:

If x == y, both stones are totally destroyed;
If x != y, the stone of weight x is totally destroyed, and the stone of weight y has new weight y-x.
At the end, there is at most 1 stone left.  Return the weight of this stone (or 0 if there are no stones left.)

 

Example 1:

Input: [2,7,4,1,8,1]
Output: 1
Explanation: 
We combine 7 and 8 to get 1 so the array converts to [2,4,1,1,1] then,
we combine 2 and 4 to get 2 so the array converts to [2,1,1,1] then,
we combine 2 and 1 to get 1 so the array converts to [1,1,1] then,
we combine 1 and 1 to get 0 so the array converts to [1] then that's the value of last stone.
 

Note:

1 <= stones.length <= 30
1 <= stones[i] <= 1000
Accepted
23,534
Submissions
37,823
"""


# the badest algorithm but still it beats 95%
def lastStoneWeight(stones):
    """
    Runtime: 32 ms, faster than 95.62% of Python3 online submissions for Last Stone Weight.
    Memory Usage: 14 MB, less than 100.00% of Python3 online submissions for Last Stone Weight.
    """
    while len(stones) >= 2:
        stones = sorted(stones, reverse=True)
        x = stones[1]
        y = stones[0]
        stones = stones[2:]+[y-x] if y-x > 0 else stones[2:]
    return stones[0] if len(stones) else 0

if __name__ == '__main__':
    s = [2,7,4,1,8,1]
    s = [1,3]
    print(lastStoneWeight(s))