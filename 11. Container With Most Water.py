class Solution:
    def maxArea(self, height: List[int]) -> int:

        max_amount = 0
        left = 0
        right = len(height) -1

        while left < right:
            smaller_height = min(height[left],height[right])
            width = right - left
            max_amount = max(max_amount, smaller_height*width )

            if height[left] > height[right]:
                right -=1
            else:
                left += 1
        
        return max_amount

        