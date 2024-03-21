# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder:
            return None

        # 获取根节点的值
        root_val = preorder[0]
        # 创建根节点
        root = TreeNode(root_val)

        # 在中序遍历中找到根节点的索引，以此为界划分左右子树
        breaker_index = inorder.index(root_val)

        # 根据根节点在中序遍历中的位置分割中序遍历序列
        inorder_left = inorder[:breaker_index]
        inorder_right = inorder[breaker_index + 1:]

        # 计算左子树的长度
        x = len(inorder_left)

        # 修正：根据左子树的长度分割前序遍历序列
        preorder_left = preorder[1:1+x]
        preorder_right = preorder[1+x:]

        # 递归构建左右子树
        root.left = self.buildTree(preorder_left, inorder_left)
        root.right = self.buildTree(preorder_right, inorder_right)

        return root

