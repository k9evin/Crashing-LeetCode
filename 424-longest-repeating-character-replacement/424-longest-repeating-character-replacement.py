class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # Solution 1:
        # Time complexity: O(26 * n)
        # Space complexity: O(n)
        l = 0
        res = 0
        count = {}
        
        for r, char in enumerate(s):
            count[char] = 1 + count.get(char, 0)
            while ((r - l + 1) - max(count.values())) > k:
                count[s[l]] -= 1
                l += 1
            res = max(res, (r - l + 1))
        return res
		
		# Solution 2:
        # Time complexity: O()
        # Space complexity: O()
		
		# Solution 3:
        # Time complexity: O()
        # Space complexity: O()