# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:

        result = []
        path = []

        if not root:
            return result

        self.traves(root,result,path)

        return result

    def traves(self, cur, result, path):

        path.append(cur.val)

        if not cur.left and not cur.right:

            spath = "->".join(map(str,path))

            result.append(spath)

        if cur.left:
            self.traves(cur.left,result,path)
            path.pop()
        if cur.right:
            self.traves(cur.right,result,path)    
            path.pop()

