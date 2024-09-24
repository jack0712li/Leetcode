class Solution:
    # Double for loop, first ly useing the first array to create a prefix map, then use the second array to find the longest common prefix
    def longestCommonPrefix(self, arr1: List[int], arr2: List[int]) -> int:
        prefix_map = {}

        for each in arr1:
            str_each = str(each)
            prefix = ""
            for char in str_each:
                prefix += char
                prefix_map[prefix] = prefix_map.get(prefix,0) +1

        result = 0
        for each in arr2:
            str_each = str(each)
            prefix = ""
            for char in str_each:
                prefix += char

                if prefix in prefix_map:
                    result = max(result, len(prefix))

        return result
    
# One better way, using set to record the prefix, reduce the space complexity
    class Solution:
    def longestCommonPrefix(self, arr1: List[int], arr2: List[int]) -> int:
        prefix_set = set()

        for each in arr1:
            str_each = str(each)
            prefix = ""
            for char in str_each:
                prefix += char
                if prefix not in prefix_set:
                    prefix_set.add(prefix)

        result = 0
        for each in arr2:
            str_each = str(each)
            prefix = ""
            for char in str_each:
                prefix += char
                if prefix in prefix_set:
                    result = max(result, len(prefix))

        return result