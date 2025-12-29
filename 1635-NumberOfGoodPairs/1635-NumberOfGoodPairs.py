# Last updated: 12/29/2025, 1:41:29 AM
class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        freq = collections.defaultdict(int)
        res = 0

        for n in nums:
            res += freq[n]
            freq[n] += 1

        return res
        
        # res = 0
        # for k, v in freq.items():
        #     if v > 1:
        #         res += v * (v - 1) // 2
        # return res