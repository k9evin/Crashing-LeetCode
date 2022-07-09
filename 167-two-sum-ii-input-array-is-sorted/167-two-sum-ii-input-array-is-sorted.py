class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # Solution 1:
        # Time complexity: O(n)
        # Space complexity: O(1)
        left, right = 0, len(numbers) - 1
        while left < right:
            while (left < right) and (numbers[left] + numbers[right] > target):
                  right -= 1
            while (left < right) and (numbers[left] + numbers[right] < target):
                  left += 1
            if (numbers[left] + numbers[right] == target):
                return [left + 1, right + 1]
		
		# Solution 2:
        # Time complexity: O()
        # Space complexity: O()
		
		# Solution 3:
        # Time complexity: O()
        # Space complexity: O()