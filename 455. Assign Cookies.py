class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()

        index_child = 0
        result = 0

        for i in range(len(s)):
            if index_child < len(g) and g[index_child] <= s[i]:
                result += 1
                index_child += 1

        return result
        

        