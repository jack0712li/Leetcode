# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
            
        self.dict = {}
        result = []
        def inorder(root):
            if not root:
                return
            inorder(root.left)
            self.dict[root.val] = self.dict.get(root.val, 0) + 1
            inorder(root.right)
        
        inorder(root)
        
        max_freq = max(self.dict.values())  

        for key, val in self.dict.items():
            if val == max_freq:
                result.append(key)
        
        return result
