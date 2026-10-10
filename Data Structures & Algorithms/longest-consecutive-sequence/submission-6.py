class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        numSet = set(nums)

        count = 0
        current = 1
        ans = 0


        for num in numSet:
            if num - 1 not in numSet:
                current = num
                count = 1

                while current + 1 in numSet:

                    count += 1
                    current += 1

                ans = max(ans, count)

        return ans




