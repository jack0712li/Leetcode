# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:


        
        cur = root
        pre = root

        new=TreeNode(val)

        if not root:
            return new

        while cur:
            if cur.val> new.val:
                pre= cur
                cur = cur.left

            else:
                cur.val<new.val
                pre= cur
                cur = cur.right

        if pre.val>new.val:
            pre.left = new
        else:
            pre.right = new
        
        return root


        