class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Solution 1:
        # Time complexity: O(nlogn)
        # Space complexity: O(n)
        # freq = {}
        # for i in nums:
        #     freq[i] = freq.get(i, 0) + 1
        # sorted_freq = dict(sorted(freq.items(), key=lambda x:x[1], reverse=True))
        # return list(sorted_freq.keys())[:k]
    
		# Solution 2:
        # Time complexity: O(n)
        # Space complexity: O(n)
        count = {}
        freq = [[] for i in range(len(nums) + 1)]
        for n in nums:
            count[n] = count.get(n, 0) + 1
        for n, f in count.items():
            freq[f].append(n)
        result = []
        for elem in range(len(freq) - 1, 0, -1):
            for i in freq[elem]:
                result.append(i)
                if len(result) == k:
                    return result
        
		# Solution 3:
        # Time complexity: O()
        # Space complexity: O()
        # return [num for num, freq in Counter(nums).most_common(k)]