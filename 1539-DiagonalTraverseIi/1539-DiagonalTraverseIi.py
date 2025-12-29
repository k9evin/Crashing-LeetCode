# Last updated: 12/29/2025, 1:41:37 AM
class Solution:
    def findDiagonalOrder(self, nums: List[List[int]]) -> List[int]:
        diagonal_map = collections.defaultdict(list)

        # 在同一个diagonal上的数, i+j 相同
        for i in range(len(nums)):
            for j in range(len(nums[i])):
                diagonal_map[i + j].append(nums[i][j])

        res = []

        for v in diagonal_map.values():
            res.extend(reversed(v))

        return res
