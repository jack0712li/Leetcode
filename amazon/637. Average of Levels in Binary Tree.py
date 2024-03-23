# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        levels =[]
        def bfs (root,level,levels):
            if not root:
                return

            if len(levels) == level:
                levels.append([])

            levels[level].append(root.val)

            bfs(root.left,level+1,levels)
            bfs(root.right,level+1,levels)

        bfs(root,0,levels)

        result = []
        for each in levels:
            result.append(sum(each)/len(each))

        return result        