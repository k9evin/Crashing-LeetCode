class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # Solution 1:
        # Time complexity: O(n)
        # Space complexity: O(1)
        length = len(s1)
        s1_dict = Counter(s1)
        s2_dict = {}
        l = 0
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
        # Time complexity: O(n)
        # Space complexity: O(1)
        # length = len(s1)
        # s1_dict = Counter(s1)
        # valid = 0
        # for r, char in enumerate(s2):
        #     # 如果滑动窗口最左边的字符在 s1_dict 中，就需要增加该字符的计数
        #     if (r >= length and s2[r - length] in s1_dict):
        #         # 如果该字符在字典中计数已经为 0 了，意味着它已经 valid 了
        #         # 又由于我们需要移除它，所以该字符不再 valid
        #         if s1_dict[s2[r - length]] == 0:
        #             valid -= 1
        #         s1_dict[s2[r - length]] += 1
        #     if char in s1_dict:
        #         s1_dict[char] -= 1
        #         if s1_dict[char] == 0:
        #             valid += 1
        #     # 如果 valid 和字典里元素的个数相符， 则所有字符都已符合要求
        #     if valid == len(s1_dict):
        #         return True
        # return False