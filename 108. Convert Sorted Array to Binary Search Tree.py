# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def sortedArrayToBST(self, nums):
        return self.gen(nums, 0, len(nums)-1)

    def gen(self, l, s, e):
        if s>e:
            return
        m = (s+e) // 2
        temp_root = TreeNode(l[m])
        # print(m, l[m])
        temp_root.left = self.gen(l, s, m-1)
        temp_root.right = self.gen(l, m+1, e)

        return temp_root


def pre_order(root):
    if root != None:
        pre_order(root.left)
        print(root.val)
        pre_order(root.right)


if __name__ == '__main__':
    ls = [-10,-3,0,5,9, 10]
    sol = Solution().sortedArrayToBST(ls)
    pre_order(sol)
