class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        """
        Finds all unique triplets in a list of integers that sum to zero

        Time Complexity: O(n^2), where n is the length of the input list
        Space Complexity: O(1) if sorting is done in-place
        """
        res = []
        # Sort the input array
        nums.sort()

        # Iterate through the array
        for i in range(len(nums)):
            # If current number is positive, break loop
            if nums[i] > 0:
                break
            # Skip duplicate numbers for the first element
            if i == 0 or nums[i] != nums[i - 1]:
                # Initialize left and right pointers
                l, r = i + 1, len(nums) - 1

                # Two-pointer approach
                while l < r:
                    three_sum = nums[i] + nums[l] + nums[r]

                    # Adjust pointers based on the sum
                    if three_sum < 0:
                        l += 1
                    elif three_sum > 0:
                        r -= 1
                    else:
                        # Add triplet to result
                        res.append([nums[i], nums[l], nums[r]])
                        l += 1
                        r -= 1
                        # Skip duplicate numbers for the second element
                        while l < r and nums[l] == nums[l - 1]:
                            l += 1

        return res
