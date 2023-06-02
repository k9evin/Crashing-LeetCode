class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left, length = 0, 0
        charSet = set()
        for right in range(len(s)):
            # keep removing the left-most character
            while s[right] in charSet:
                charSet.remove(s[left])
                left += 1
            charSet.add(s[right])
            length = max(length, right - left + 1)
        return length
    # O(n), the space complexity is O(1) because we have 
    # limited numbers of letters, digits, etc
