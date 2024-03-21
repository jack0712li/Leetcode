# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:

        stack=[]
        restult = float('inf')
    
        def inorder(root):

            if not root:
                return

            
            inorder(root.left)
            stack.append(root.val)
            inorder(root.right)

        inorder(root)

        for i in range(len(stack)-1):
            restult = min(restult,abs(stack[i+1]-stack[i]))


        return restult