# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        results =[]
        path = []

        def helper(root,old_sum,old_path):
            if not root:
                return 
            

            new_path=old_path + [root.val]


            new_sum = old_sum + root.val
            if new_sum == targetSum and root.left == None and root.right == None:
                results.append(new_path)
            else:
                helper(root.left,new_sum,new_path)
                helper(root.right,new_sum,new_path)


        helper(root,0,path)
        return results

            