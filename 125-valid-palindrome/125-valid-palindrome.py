class Solution:
    def isPalindrome(self, s: str) -> bool:
        # Solution 1:
        # Time complexity: O()
        # Space complexity: O()
        string = "".join(filter(str.isalnum, s)).upper()
        left, right = 0, len(string) - 1
        while left < right:
            if string[left] != string[right]:
                return False
            left += 1
            right -= 1
        return True
        
		
		# Solution 2:
        # Time complexity: O()
        # Space complexity: O()
		
		# Solution 3:
        # Time complexity: O()
        # Space complexity: O()