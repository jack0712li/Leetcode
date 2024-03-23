# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False

        def helper(root,sum):
            if not root:
                return False
            sum += root.val
            if not root.left and not root.right:
                return sum == targetSum

            
            return helper(root.left,sum) or helper(root.right,sum)


        return helper(root,0)
        
        