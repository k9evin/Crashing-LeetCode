class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # Solution 1:
        # Time complexity: O(logn)
        # Space complexity: O(1)
        arrayTop = 0
        arrayBot = len(matrix) - 1
        row = -1
        while arrayTop <= arrayBot:
            row = (arrayTop + arrayBot) // 2
            if target > matrix[row][-1]:
                arrayTop = row + 1
            elif target < matrix[row][0]:
                arrayBot = row - 1
            else:
                break
        
        l = 0
        r = len(matrix[row]) - 1
        while l <= r:
            m = (l + r) // 2
            if target < matrix[row][m]:
                r = m - 1
            elif target > matrix[row][m]:
                l = m + 1
            else:
                return True
        return False        
		
		# Solution 2:
        # Time complexity: O()
        # Space complexity: O()
		
		# Solution 3:
        # Time complexity: O()
        # Space complexity: O()