class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # Solution 1:
        # Time complexity: O()
        # Space complexity: O()
        length = len(s1)
        s1_dict = Counter(s1)
        s2_dict = {}
        l, r = 0, 0
        count = 0
        for r, char in enumerate(s2):
            if s2_dict == s1_dict:
                return True
            if (count >= length and s2_dict != s1_dict):
                s2_dict[s2[l]] -= 1
                if s2_dict[s2[l]] == 0:
                    del s2_dict[s2[l]]
                l += 1
                count -= 1
            s2_dict[char] = s2_dict.get(char, 0) + 1
            count += 1 
        return s2_dict == s1_dict
            
            
            
                
            
            
		# Solution 2:
        # Time complexity: O()
        # Space complexity: O()
		
		# Solution 3:
        # Time complexity: O()
        # Space complexity: O()