# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:


        def helper(root,old_sum):
            if not root:
                return False



            new_sum = old_sum + root.val
            if new_sum == targetSum and root.left == None and root.right == None:
                return True

            left = helper(root.left,new_sum)
            right = helper(root.right,new_sum)

            return left or right

        return helper(root,0)
        