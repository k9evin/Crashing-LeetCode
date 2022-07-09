class Solution:
    def isPalindrome(self, s: str) -> bool:
        # Solution 1:
        # Time complexity: O(n)
        # Space complexity: O(n)
        # string = "".join(filter(str.isalnum, s)).upper()
        # left, right = 0, len(string) - 1
        # while left < right:
        #     if string[left] != string[right]:
        #         return False
        #     left += 1
        #     right -= 1
        # return True
		
		# Solution 2:
        # Time complexity: O(n)
        # Space complexity: O(1)
        left, right = 0, len(s) - 1
        while left < right:
            # skip non-alphanumeric characters
            while left < right and not s[left].isalnum():
                left += 1
            while left < right and not s[right].isalnum():
                right -= 1
            if s[left].lower() != s[right].lower():
                return False
            left += 1
            right -= 1
        return True