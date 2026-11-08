class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows = len(matrix)
        cols = len(matrix[0])

        total = rows * cols

        left = 0
        right = total - 1

        while left <= right:

            mid = left + ((right - left)) // 2
            
            i = mid // cols
            j = mid % cols

            mid_num = matrix[i][j]

            if mid_num == target:
                return True
            elif target < mid_num:
                right = mid - 1
            else:
                left = mid + 1

        return False
