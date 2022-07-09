class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # Solution 1:
        # Time complexity: O(n)
        # Space complexity: O(1)
        left, right = 0, len(numbers) - 1
        while left < right:
            curr = numbers[left] + numbers[right]
            if curr > target:
                  right -= 1
            elif curr < target:
                  left += 1
            else:
                return [left + 1, right + 1]
        return []