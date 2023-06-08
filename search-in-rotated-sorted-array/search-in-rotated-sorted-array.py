class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1

        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            # 此时左半边一定有序，右半边可能有序可能部分有序
            elif nums[left] <= nums[mid]:
                # target在左边范围内，缩小范围
                if nums[left] <= target < nums[mid]:
                    right = mid - 1
                # target在右边范围内，left移到右半边
                else:
                    left = mid + 1
            # 此时右半边一定有序，左半边可能有序可能部分有序
            else:
                # target在右边范围内，缩小范围
                if nums[mid] < target <= nums[right]:
                    left = mid + 1
                # target在左边范围内，right移到右半边
                else:
                    right = mid - 1
        return -1
