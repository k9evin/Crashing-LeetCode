class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Solution 1:
        # Time complexity: O(nlogn)
        # Space complexity: O(n)
        freq = {}
        for i in nums:
            freq[i] = freq.get(i, 0) + 1
        sorted_freq = dict(sorted(freq.items(), key=lambda x:x[1], reverse=True))
        return list(sorted_freq.keys())[:k]
    
		# Solution 2:
        # Time complexity: O()
        # Space complexity: O()
		
		# Solution 3:
        # Time complexity: O()
        # Space complexity: O()