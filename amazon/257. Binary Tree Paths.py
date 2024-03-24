# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        if not root:
            return[]

        result = []
        
        self.backtracking(root,[],result)
        return result


    def backtracking(self,root,path,result):
        if not root:
            return
        if not root.left and not root.right:
            path.append(str(root.val))
            str_path = "->".join(path)
            path.pop()
            result.append(str_path)
            return
        path.append(str(root.val))
        if root.left:
            self.backtracking(root.left,path,result)
        if root.right:
            self.backtracking(root.right,path,result)
        path.pop()
    
