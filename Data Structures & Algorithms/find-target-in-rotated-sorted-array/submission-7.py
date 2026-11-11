class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1

        while left < right:
            mid = (left + right) // 2

            if nums[mid] > nums[right]:
                left = mid + 1
            else:
                right = mid

        pivot = right

        def binarySearch(left:int, right:int) -> int:

            while left <= right:
                midpoint = (left + right ) // 2

                if nums[midpoint] == target:
                    return midpoint
                elif nums[midpoint] < target:
                    left = midpoint + 1
                else:
                    right = midpoint - 1
 
            return -1 


        result = binarySearch(0, pivot -1)

        if result != -1:
            return result

        return binarySearch(pivot, len(nums)-1)



            
       
        




