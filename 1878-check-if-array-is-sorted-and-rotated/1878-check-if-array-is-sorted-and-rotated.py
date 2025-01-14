class Solution:
    def check(self, nums: List[int]) -> bool:
        """
        Algorithm:
        - Traverse the array and count how many times the order is "broken" (i.e., nums[i-1] > nums[i]).
        - The array can only be considered a rotated sorted array if the order breaks at most once.
        - If the count of breaks is ≤ 1, return True; otherwise, return False.

        Time Complexity: O(n), where n is the length of the array.
        Space Complexity: O(1), as no additional space is used.
        """
        count = 0  # Counter for the number of order breaks

        # Iterate through the array, checking each pair of elements
        for i in range(len(nums)):
            # If the previous element is greater than the current, increment count
            if nums[i - 1] > nums[i]:
                count += 1

        # Return True if there is at most one order break
        return count <= 1
