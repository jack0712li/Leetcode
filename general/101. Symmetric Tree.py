# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:

        if not root:
            return True
        
        return self.compare(root.left,root.right)

    def compare(self, root_left , root_right) :


        if root_left == None and root_right != None:
            return False
        elif root_left != None and root_right == None:
            return False
        elif not root_left and not root_right:
            return True
        elif root_left.val != root_right.val:
            return False


        outside = self.compare(root_left.left,root_right.right)
        inside = self.compare(root_left.right,root_right.left)

        return outside and inside
        