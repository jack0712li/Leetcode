class Solution:
    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:
        if len(original) != n *m:
            return []
        result = []
        for i in range(0,len(original),n):
            result.append(original[i:n+i])

        return result