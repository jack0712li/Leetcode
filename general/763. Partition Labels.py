class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        last_ocur = {}
        for i, char in enumerate(s):
            last_ocur[char] = i


        result = []
        start = 0
        end = 0
        for i, char in enumerate(s):
            end = max(end,last_ocur[char])
            if end == i:
                result.append(end-start +1)
                start = end +1
        
        return result
