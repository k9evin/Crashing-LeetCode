# Last updated: 12/29/2025, 1:40:57 AM
class Solution:
    def countNicePairs(self, nums: List[int]) -> int:
        MOD = 10**9+7
        freq = collections.defaultdict(int)
        count = 0

        for n in nums:
            key = n - int(str(n)[::-1])
            # we dont need to check if key is in the map, because it will return 0 if not exist
            count += freq[key]
            freq[key] += 1
        
        return count % MOD