class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = 0
        length = 0
        maxFreq = 0
        freqMap = {}
        for right in range(len(s)):
            freqMap[s[right]] = freqMap.get(s[right], 0) + 1
            # keep track of the max frequency
            maxFreq = max(maxFreq, freqMap[s[right]])
            # if length - maxFreq <= k, meaning that the current
            # window is valid
            if (right - left + 1) - maxFreq <= k:
                # compute the max length
                length = max(length, right - left + 1)
            # if not valid, then decrement the count and move the 
            # left pointer to the right
            else:
                freqMap[s[left]] -= 1
                left += 1
        return length
    # O(n), O(1)