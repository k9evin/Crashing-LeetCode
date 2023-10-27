class Solution:
    def longestPalindrome(self, s: str) -> str:
        
        def palindrom(s, l, r):
            # check if they are within bound and palindrom
            while l >= 0 and r < len(s) and s[l] == s[r]:
                l -= 1
                r += 1
            # when we are out of the loop, s[l] != s[r],
            # so we need to use the previous l, r values
            return s[l+1: r]

        res = ''
        for i in range(len(s)):
            # if the length of str is odd
            odd = palindrom(s, i, i)
            # if the length of str is even
            even = palindrom(s, i, i + 1)

            # the longest str will be the result
            res = max(res, odd, even, key=len)
            
        return res