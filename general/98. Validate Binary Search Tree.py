# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        stack =[]
        
        def dfs(root):

            if not root:
                return

            dfs(root.left)
            stack.append(root.val)
            dfs(root.right)
        dfs(root)
        for i in range(len(stack)-1):

            if stack[i] >= stack[i+1]:
                return False

        return True



        # Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.max_val = float('-inf')
        self.result = True


    def isValidBST(self, root: Optional[TreeNode]) -> bool:

  

        
        def dfs(root):

            if not root:
                return

            dfs(root.left)

            if root.val <= self.max_val:
                self.result = False

            self.max_val = root.val

            dfs(root.right)
        dfs(root)

        return self.result

