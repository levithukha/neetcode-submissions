class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0
        
        n = len(height)
        left = 0
        right = n - 1
        leftmax = height[left]
        rightmax = height[right]
        res = 0

        while left < right:
            if leftmax < rightmax:
                left += 1
                leftmax = max(leftmax, height[left])
                res += leftmax - height[left]
            else:
                right -= 1
                rightmax = max(rightmax, height[right])
                res += rightmax - height[right]

        return res
