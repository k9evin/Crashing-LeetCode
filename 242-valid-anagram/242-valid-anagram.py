class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # Solution 1:
        # Time complexity: O(n)
        # Space complexity: O(1)
        if len(s) != len(t):
            return False
        # using hashmap
        counter = {}
        for char in s:
            counter[char] = counter.get(char, 0) + 1
        for char in t:
            if char in counter:
                counter[char] -= 1
            else:
                return False
        # make sure all the values are 0
        for val in counter.values():
            if val != 0:
                return False
        return True
		
		# Solution 2:
        # Time complexity: O()
        # Space complexity: O()
		
		# Solution 3:
        # Time complexity: O()
        # Space complexity: O()