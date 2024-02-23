# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:

        if not nums:
            return

        root_val = max(nums)
        root = TreeNode(root_val)

        index = nums.index(root_val)

        left_nums = nums[:index]
        right_nums = nums[index+1:]

        root.left = self.constructMaximumBinaryTree(left_nums)
        root.right = self.constructMaximumBinaryTree(right_nums)

        return root
