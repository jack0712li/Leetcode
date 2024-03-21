# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:

        left = 10001
        right = 10001

        if not root:
            return 0

        if root.left == None and root.right ==None:
            return 1

        if root.left != None:
            left = self.minDepth(root.left)

        if root.right != None:
            right = self.minDepth(root.right)

        return min(left,right) +1





        