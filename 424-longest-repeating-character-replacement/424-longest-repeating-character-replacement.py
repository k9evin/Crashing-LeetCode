class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # Solution 1:
        # Time complexity: O(26 * n)
        # Space complexity: O(n)
        # l = 0
        # res = 0
        # count = {}
        # for r, char in enumerate(s):
        #     count[char] = 1 + count.get(char, 0)
        #     while ((r - l + 1) - max(count.values())) > k:
        #         count[s[l]] -= 1
        #         l += 1
        #     res = max(res, (r - l + 1))
        # return res
		
		# Solution 2:
        # Time complexity: O()
        # Space complexity: O()
        l = 0
        res = 0
        max_freq = 0
        count = {}
        
        for r, char in enumerate(s):
            count[char] = 1 + count.get(char, 0)
            max_freq = max(max_freq, count[char])
            while ((r - l + 1) - max_freq) > k:
                count[s[l]] -= 1
                l += 1
            res = max(res, (r - l + 1))
        
        return res
		