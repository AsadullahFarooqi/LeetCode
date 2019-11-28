# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root == None:
            return -1
        left = maxDepth(root.left)
        right = maxDepth(root.right)

        return max(left, right) + 1
        

if __name__ == '__main__':
    sol = Solution().maxDepth(r)
